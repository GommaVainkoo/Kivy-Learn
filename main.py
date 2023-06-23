
from kivy.app import App
from kivy.graphics import Line, Color, Rectangle,Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image

class CanvaExample7(BoxLayout):
    pass
class CanvaExample5(Widget):
    pass
class CanvaExample4(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.vx=dp(3)
        self.vy=dp(4)

        with self.canvas:
            #self.ball=Image(source="images/cake.jpg")
            self.ball=Ellipse(size=(dp(50),dp(50)),pos=self.center)
            Clock.schedule_interval(self.update,1/120)
    def on_size(self,*args):
        self.ball.pos= (self.center_x-25,self.center_y-25)
    def update(self,dt):
        x,y=self.ball.pos
        x=x+self.vx
        y=y+self.vy
        if(y+50>self.height):
            y=self.height-50
            self.vy=-self.vy
        if(x+50>self.width):
            x=self.width-50
            self.vx=-self.vx
        if(x<0):
            self.vx=-self.vx
        if (y < 0):
            self.vy = -self.vy
        self.ball.pos=(x,y)


class CanvaExample3(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(0,100,100,0),width=2)
            Color(1,0,1)
            self.rect1=Rectangle(pos=(500,250),size=(150,20))
    def move_rect(self):
        w=self.width
        x1, y1 = self.rect1.pos
        w1,h1=self.rect1.size
        w2=x1+w1
        if(w2+10<=w):
            x1+=dp(10)
            self.rect1.pos=(x1,y1)
class CanvaExample(Widget):
    pass
class CanvaExample1(Widget):
    pass
class CanvaExample2(Widget):
    pass
class PageLayouts(GridLayout):
    text_on=StringProperty("0")
    slider_value=StringProperty("-")
    message=StringProperty("")
    count=0
    code=BooleanProperty(True)
    def on_toggle_state(self,state):
        print(state.state)
        if state.state=="normal":
            state.text="Off"
            self.code=True
        else:
            state.text="On"
            self.code=False
    def on_presss(self):
        if self.code==False:
            self.count=self.count+1
            self.text_on = str(self.count)
    def get_slider_value(self,gomma):
        self.slider_value=str(int(gomma.value))
    def on_text_enter(self,enter):
        self.message=enter.text



class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(0,100):
            b=Button(text="Button"+str(i+1),size_hint=(None,None),size=(dp(120),dp(100)))
            self.add_widget(b)
class GridLayoutExample(GridLayout):
    pass
class LayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class ShakthiApp(App):
    pass

ShakthiApp().run()

