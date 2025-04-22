
# 导入GUI库kivy
# 导入标签类
from kivy.uix.label import Label
# 导入按钮类
from kivy.uix.button import Button
# 导入布局管理类
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# 导入屏幕类
from kivy.uix.screenmanager import Screen, ScreenManager
# 功能提供可视的交互功能
from kivy.app import App
# 导入卦包
import func.guafunction as fg
from kivy.core.text import LabelBase



# 注册字体（开发环境路径）
def register_fonts():
    # 注册第一种字体
    LabelBase.register(
        name="simhei",  # 自定义字体名称
        fn_regular="fonts/simhei.ttf"  # 字体文件路径
    )
    # 注册第二种字体
    LabelBase.register(
        name="NotoSansSCMedium",
        fn_regular="fonts/NotoSansSCMedium-4.ttf"
    )

# 调用注册函数
register_fonts()

class MyApp(App):
    def build(self):
        sm=ScreenManager()
        main=MainScreen(name='main')
        minor=MinorScreen(name='minor')
        sm.add_widget(main)
        sm.add_widget(minor)
        return sm
    
class MainScreen(Screen):
    #初始化布局
    def __init__(self,**kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # 创建标签
        title= Label(text="抽签结果", font_size=50,font_name='simhei',halign='center',valign='middle')
        # 创建按钮
        start = ButtonStart()
        button1 = ChangeYaoButton("1", lambda *args: self.gominor("1", *args))
        button2 = ChangeYaoButton("2", lambda *args: self.gominor("2", *args))
        button3 = ChangeYaoButton("3", lambda *args: self.gominor("3", *args))
        button4 = ChangeYaoButton("4", lambda *args: self.gominor("4", *args))
        button5 = ChangeYaoButton("5", lambda *args: self.gominor("5", *args))
        button6 = ChangeYaoButton("6", lambda *args: self.gominor("6", *args))
        
        # 创建垂直布局
        vlayout = BoxLayout(orientation="vertical")
        # 创建水平布局
        hlayout = BoxLayout(orientation="horizontal")
        # 结合前面两个布局
        tlayout = BoxLayout(orientation="vertical")
        # 向 vlayout 中添加按钮
        vlayout.add_widget(button6)
        vlayout.add_widget(button5)
        vlayout.add_widget(button4)
        vlayout.add_widget(button3)
        vlayout.add_widget(button2)
        vlayout.add_widget(button1)
        # 向 hlayout 中添加标签和 vlayout
        hlayout.add_widget(start.newlable)
        hlayout.add_widget(vlayout)
        # 向 tlayout 中添加 hlayout 和 button0
        tlayout.add_widget(title)
        tlayout.add_widget(hlayout)
        tlayout.add_widget(ButtonStart.meanlable)
        tlayout.add_widget(start)
        # 向屏幕中添加 tlayout
        self.add_widget(tlayout)

    def gominor(self,number,*args):
        self.manager.current='minor'
        self.manager.get_screen('minor').update_label(number)

class MinorScreen(Screen):
    id = {"1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆"}
    titlelabel=Label(font_name='simhei',font_size="50",halign='center',valign='middle', pos=(36, 300))
    changelabel=Label(text="请点击变爻按钮",font_name='NotoSansSCMedium-4',font_size=68,halign='center',valign='middle',pos=(36, 50))
    meanlabel=Label(font_name='simhei',font_size="32",halign='center',valign='middle',pos=(36, -200))
    def __init__(self, **kwargs):
        super(MinorScreen,self).__init__(**kwargs)
        backb=Button(text="返回",font_size="20",font_name="simhei",on_press=self.back,size_hint=(0.2, 0.1), pos=(50, 650))
        vlayout = FloatLayout()
        vlayout.add_widget(backb)
        vlayout.add_widget(self.titlelabel)
        vlayout.add_widget(self.changelabel)
        vlayout.add_widget(self.meanlabel)
        self.add_widget(vlayout)

    def back(self,*args):
        self.manager.current = 'main'

    def update_label(self,number):
        c=fg.gua_find(number)
        self.titlelabel.text=f"变第{self.id[number]}爻"
        self.changelabel.text=f"{c[0]}"
        self.meanlabel.text=f"{c[1]}"


class ChangeYaoButton(Button):
    id = {"1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆"}

    def __init__(self, number,f,**kwargs):
        super(ChangeYaoButton, self).__init__(**kwargs)  # 调用父类的 __init__
        self.number = number
        self.text = f"变第{self.id[number]}爻"  # 设置按钮文本
        self.font_size = 14
        self.font_name='simhei'
        self.bind(on_press=f)  # 绑定点击事件

class ButtonStart(Button):
    newlable = Label(text="未抽签", font_size=62,font_name='NotoSansSCMedium-4',halign='center',valign='middle')
    meanlable = Label(text="请先抽签", font_size=32,font_name='simhei',halign='center',valign='middle')

    def __init__(self, **kwargs):
        super(ButtonStart, self).__init__(**kwargs)  # 调用父类的 __init__
        self.text = "开始抽签"
        self.font_size = 32
        self.font_name='simhei'
        self.bind(on_press=self.on_button_click)  # 绑定点击事件

    def on_button_click(self,*args):
        c=fg.rand_gua()
        self.newlable. text=f"{c[0]}"
        self.meanlable.text=f"{c[1]}"

if __name__ == "__main__":
    MyApp().run()
