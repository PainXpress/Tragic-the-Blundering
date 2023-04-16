import requests
import wx


class DeckBuilder(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 600))

        # Create a scrollable panel to hold the card list
        self.panel = wx.ScrolledWindow(self)
        self.panel.SetScrollbars(1, 1, 1, 1)
        self.panel.Bind(wx.EVT_SIZE, self.OnSize)
        self.panel.Bind(wx.EVT_SCROLLWIN, self.OnScroll)

        # Create a grid to hold the cards
        self.card_grid = wx.GridSizer(cols=5, hgap=10, vgap=10)

        # Create a search field and button
        self.search_label = wx.StaticText(self, label="Search for a card:")
        self.search_field = wx.TextCtrl(self)
        self.search_button = wx.Button(self, label="Search")
        self.search_button.Bind(wx.EVT_BUTTON, self.OnSearch)

        # Create a button to add the selected cards to the deck
        self.add_button = wx.Button(self, label="Add to Deck")
        self.add_button.Bind(wx.EVT_BUTTON, self.OnAdd)

        # Create a button to close the deck builder window
        self.close_button = wx.Button(self, label="Close")
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClose)

        # Create a horizontal box sizer to hold the search field and button
        self.search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.search_sizer.Add(self.search_label, 0, wx.ALL, 10)
        self.search_sizer.Add(self.search_field, 1, wx.ALL | wx.EXPAND, 10)
        self.search_sizer.Add(self.search_button, 0, wx.ALL, 10)

        # Create a horizontal box sizer to hold the add and close buttons
        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button_sizer.Add(self.add_button, 0, wx.ALL, 10)
        self.button_sizer.Add(self.close_button, 0, wx.ALL, 10)

        # Create a vertical box sizer to hold the panel, search field and buttons
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 1, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.search_sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.button_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Set the sizer for the frame
        self.SetSizer(self.sizer)

    def OnSearch(self, event):
        # Clear the existing card grid
        for child in self.card_grid.GetChildren():
            self.card_grid.Detach(child.Window)
            child.Window.Destroy()

        # Make a request to the Scryfall API to retrieve the card search results
        search_term = self.search_field.GetValue()
        response = requests.get("https://api.scryfall.com/cards/search", params={"q": search_term})

        # Parse the JSON data in the response
        card_data = response.json()

        # Create a button for each card in the search results
        for card in card_data["data"]:
            button = wx.Button(self.panel, label=card["name"])
            button.Bind(wx.EVT_BUTTON, self.OnButtonClick)
            self.card_grid.Add(button)

        # Add the grid to the panel
        self.panel.SetSizer(self.card_grid)

    def OnButtonClick(self, event):
        button = event.GetEventObject()
        card_name = button.GetLabel()
        # Make a request to the Scryfall API to retrieve the details of the selected card
        response = requests.get("https://api.scryfall.com/cards/named", params={"exact": card_name})
        card_data = response.json()
        # Create a new panel to display the card image and details
        card_panel = wx.Panel(self)
        card_panel.SetBackgroundColour(wx.WHITE)
        # Create a sizer to arrange the card elements vertically
        card_sizer = wx.BoxSizer(wx.VERTICAL)
        # Add the card image to the sizer
        card_image = wx.StaticBitmap(card_panel, wx.ID_ANY, wx.NullBitmap)
        image_url = card_data["image_uris"]["normal"]
        image_data = requests.get(image_url).content
        card_image.SetBitmap(wx.Bitmap.FromBuffer(304, 420, image_data))
        card_sizer.Add(card_image, 0, wx.ALL, 10)
        # Add the card name and details to the sizer
        card_title = wx.StaticText(card_panel, label=card_data["name"])
        card_sizer.Add(card_title, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        card_details = wx.StaticText(card_panel, label=card_data["oracle_text"])
        card_details.Wrap(700)
        card_sizer.Add(card_details, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        # Add the sizer to the panel
        card_panel.SetSizer(card_sizer)
        # Add the panel to the deck builder sizer
        self.sizer.Insert(len(self.sizer.GetChildren()) - 1, card_panel, 0, wx.EXPAND | wx.ALL, 10)
        self.Layout()
