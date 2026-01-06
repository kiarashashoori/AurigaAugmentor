from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window

import os

class app(App):
    def on_start(self):
        Window.size = (1100, 600)
        Window.minimum_width = 800
        Window.minimum_height = 600

    def build(self):
        options = ['increase brightness', 'decrease brightness' ,'increase contrast',
                   'decrease contrast','decrease saturation' , 'increase saturation' ,
                   'salt&pepper', 'blur', 'vertical motion blur', 'horizental motion blur',
                   'shadow', 'sunlight', 'rotate' , 'flipped' , 'hue']

        checkbox_layout = StackLayout(orientation ='lr-tb')
        for i in range(len(options)):
            lbl = Label(text=options[i],size_hint = (None,None),size = ("150dp", "100dp"), halign='left',valign='middle',pos_hint = (None,None))
            chk = CheckBox(active=False,size_hint = (None,None),pos_hint = (None,None))
            checkbox_layout.add_widget(lbl)
            checkbox_layout.add_widget(chk)



        
        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='start',size_hint = (None,None),size = ("75dp","40dp"),background_normal='',background_color=(0,0.8,0.3,1))
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)

        screen_layout = FloatLayout()
        screen_layout.add_widget(confirm_layout)
        screen_layout.add_widget(checkbox_layout)
        screen_layout.add_widget(image_layout)
        return screen_layout
    

class PathBrowserApp(App):
    def on_start(self):
        Window.minimum_width = 1000
        Window.minimum_height = 600
        Window.size = (1000, 600)
        
        

    def build(self):
        #tb_values = [input_image,input_label,output_image,output_label]
        tb_values = ['ss','','','']
        floatlayout = FloatLayout()
        input_img_lbl = Label(text='input image path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,415))

        input_img_tb = TextInput(text = tb_values[0],size_hint = (None,None),size=("600dp","30dp"),pos=(200,450),
                                 multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))
        
        browse_input_img = Button(text='browse',size_hint = (None,None),size=("100dp","20dp"),pos=(800,455))

        input_label_lbl = Label(text='input label path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,315))

        input_label_tb = TextInput(text = tb_values[1],size_hint = (None,None),size=("600dp","30dp"),pos=(200,350),
                                   multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))

        browse_input_label = Button(text='browse',size_hint = (None,None),size=("100dp","20dp"),pos=(800,355))

        output_img_lbl = Label(text='output image path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,215))

        output_img_tb = TextInput(text = tb_values[2],size_hint = (None,None),size=("600dp","30dp"),pos=(200,250),
                                  multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))

        browse_output_img = Button(text='browse',size_hint = (None,None),size=("100dp","20dp"),pos=(800,255))
        
        output_label_lbl = Label(text='output label path:',size_hint = (None,None),color=(1,1,1,1),pos=(50,115))

        output_label_tb = TextInput(text = tb_values[3],size_hint = (None,None),size=("600dp","30dp"),pos=(200,150),
                                    multiline=False,foreground_color=(1,1,1,1),background_normal='',background_color=(0.2,0.2,0.2,1))

        browse_output_label = Button(text='browse',size_hint = (None,None),size=("100dp","20dp"),pos=(800,155))

        lbl_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        lbl = Label(text='select your paths :',size_hint = (None,None),color=(1,1,1,1))
        lbl_layout.add_widget(lbl)

        confirm_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        confirm_btn = Button(text='confirm',size_hint = (None,None),size = ("75dp","40dp"),background_normal='',background_color=(0,0.8,0.3,1))
        confirm_layout.add_widget(confirm_btn)

        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        auriga_image = Image(source = 'Auriga.png',size_hint = (None,None))
        image_layout.add_widget(auriga_image)

        floatlayout.add_widget(input_img_lbl)
        floatlayout.add_widget(browse_input_img)
        floatlayout.add_widget(input_img_tb)
        floatlayout.add_widget(input_label_lbl)
        floatlayout.add_widget(browse_input_label)
        floatlayout.add_widget(input_label_tb)
        floatlayout.add_widget(output_img_lbl)
        floatlayout.add_widget(browse_output_img)
        floatlayout.add_widget(output_img_tb)
        floatlayout.add_widget(output_label_lbl)
        floatlayout.add_widget(browse_output_label)
        floatlayout.add_widget(output_label_tb)
        floatlayout.add_widget(confirm_layout)
        floatlayout.add_widget(image_layout)
        floatlayout.add_widget(lbl_layout)

        # Button to open popup
        # open_btn = Button(
        #     text='Open Path Browser',
        #     size_hint=(0.5, 0.2),
        #     pos_hint={'center_x': 0.5},
        #     on_press=self.open_path_browser
        # )
        
        # # Label to show selected path
        # self.path_label = Label(
        #     text='No path selected',
        #     size_hint=(1, 0.1),
        #     font_size='16sp'
        # )
        
        # main_layout.add_widget(open_btn)
        # main_layout.add_widget(self.path_label)
        
        return floatlayout
    
    def open_path_browser(self, instance):
        """Open popup with path chooser"""
        # Create main layout for popup
        popup_layout = BoxLayout(orientation='vertical', spacing=10)
        
        # ========== PATH CHOOSER SECTION ==========
        # Create file chooser
        file_chooser = FileChooserListView(
            path=os.path.expanduser('~'),  # Start at home directory
            dirselect=True,  # Allow folder selection
            filters=['*.png', '*.jpg', '*.jpeg'],  # Optional: filter for images
            size_hint=(1, 0.8)
        )
        
        # ========== CONTROL BUTTONS ==========
        button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        
        # Select button
        select_btn = Button(
            text='Select',
            on_press=lambda x: self.select_path(file_chooser)
        )
        
        # Cancel button
        cancel_btn = Button(
            text='Cancel',
            on_press=self.close_popup
        )
        
        button_layout.add_widget(select_btn)
        button_layout.add_widget(cancel_btn)
        
        # ========== IMAGE SECTION ==========
        image_layout = AnchorLayout(anchor_x='right', anchor_y='bottom', size_hint=(1, 0.1))
        
        # Check if image exists, otherwise use a placeholder
        if os.path.exists('Auriga.png'):
            auriga_image = Image(source='Auriga.png', size_hint=(None, None), size=('64dp', '64dp'))
        else:
            # Create a placeholder label if image doesn't exist
            auriga_image = Label(text='Logo', size_hint=(None, None), size=('64dp', '64dp'))
        
        image_layout.add_widget(auriga_image)
        
        # Add all sections to popup layout
        popup_layout.add_widget(file_chooser)
        popup_layout.add_widget(button_layout)
        popup_layout.add_widget(image_layout)
        
        # Create and open popup
        self.popup = Popup(
            title="Select Path",
            content=popup_layout,
            size_hint=(0.9, 0.9),  # Relative to window size
            auto_dismiss=False  # Don't close when clicking outside
        )
        self.popup.open()
    
    def select_path(self, filechooser):
        """Handle path selection"""
        if filechooser.selection:
            selected_path = filechooser.selection[0]
            self.path_label.text = f"Selected: {selected_path}"
            print(f"Selected path: {selected_path}")
            self.close_popup()
        else:
            print("No path selected")
    
    def close_popup(self, *args):
        """Close the popup"""
        if hasattr(self, 'popup'):
            self.popup.dismiss()

if __name__ == '__main__':
    root = PathBrowserApp()
    root.run()

