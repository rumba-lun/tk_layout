from tkinter import *

x,y = 0,0
ind=1
def refresh():
    canvas.create_rectangle(0, 0, canvas.winfo_width(),
                            canvas.winfo_height(), fill=TRANSCOLOUR,
                            outline=TRANSCOLOUR)
    canvas.create_polygon((80,150),(370,150),(430,365),(25,365)
                              ,fill = '#FF4081', width = 0,tags=('LabelRect'))
    canvas.tag_bind('LabelRect',"<Button-1>",Cavas_Click)
    canvas.tag_bind('LabelRect',"<ButtonRelease-1>",Cavas_Release)
    canvas.tag_bind('LabelRect',"<B1-Motion>",OnMotion)
    canvas.create_image(200,100,image=fi,anchor="nw")
    update(1)
    tk.after(100, refresh)
def Cavas_Click(event):
    global x, y
    x = event.x
    y = event.y
    print('开始移动')
def Cavas_Release(event):
    x = None
    y = None
def OnMotion(event) :
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    _x = tk.winfo_x() + deltax
    _y = tk.winfo_y() + deltay
    tk.geometry( "+%s+%s" % (_x, _y))
def update(flags):
    global ind
##    print(ind)
    if flags:
        try:
            canvas.delete('imageC')
            if (ind == framenum-1):#
                ind = 0
            frame = frames[ind]    
            image1 = canvas.create_image((80,220),image=frame,anchor='w',tags='imageC')
            ind += 1
        except:
            pass
if __name__ == '__main__':
    fip="eng.png"#你的透明背景图片位置
    TRANSCOLOUR = 'gray'

    tk = Tk()
    fi=PhotoImage(file=fip)
    tk.geometry('500x400+500+150')
    tk.title('透明窗体')
    tk.overrideredirect( True)
##    tk.wm_attributes("-topmost", True)    #窗口置顶
##    tk.wm_attributes("-disabled", True)   #窗口禁动
    tk.wm_attributes('-transparentcolor', TRANSCOLOUR)
    tk['bg'] = TRANSCOLOUR

    canvas = Canvas(tk,highlightthickness=0)
    canvas.pack(fill=BOTH, expand=Y)
    L1 = Frame(canvas)
    B1 = Button(L1,text='点击登录')
    B1.place(relx=0,rely=0,relwidth=1,relheight=1)
    W1 = canvas.create_window((100,300),window=L1,anchor='w',width=120,height=30)

    tk.after(0, refresh)    #自动刷新

    framenum = 8 # gif 的帧数需要确定下来
    giffile = 'head3.gif' #找一张白色背景的gif，设置白色为透明
    frames = [PhotoImage(file=giffile,format = 'gif -index %s' % i) for i in range(framenum)]

    tk.mainloop()
