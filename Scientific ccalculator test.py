from tkinter import*
import math

#rootvariable

root=Tk()
root.title("Calculator")

#input field

input=Entry(root, width=50, fg="white", bg="black")
input.grid(row=0, column=0,columnspan=5, ipadx=86, ipady=10)

# creating user defined functions
def button(num):
		new=input.get()
		input.delete(0,END)
		input.insert(0,str(new)+str(num))
def clear():
	input.delete(0,END)
def equal():
	cal=input.get()
	x=eval(cal)
	input.delete(0,END)
	input.insert(0, x)
#Defining scientifc tools : 
def sci():
    global b_nor
    global b_sin
    global b_cos
    global b_tan
    global b_log
    
    #Creating sci buttons
    b_nor=Button(root, text ="Nor", command=nor , padx=107, pady=25)                         
    b_log=Button(root, text="log", command= scilog, padx=42,pady=25,bg="grey", fg="white")
    b_sin=Button(root, text="sin", command= sin, padx=44,pady=25,bg="grey", fg="white")
    b_cos=Button(root, text="cos", command= cos, padx=43,pady=25,bg="grey", fg="white")
    b_tan=Button(root, text="tan", command= tan, padx=44,pady=25,bg="grey", fg="white")
    b_expo=Button(root,text="^", command=lambda:button("**"), padx=49,pady=25,bg="grey", fg="white")
    
    #placing sci buttons(overlapping with operations)
    b_nor.grid(row=1, column = 0, columnspan=2)
    b_expo.grid(row=5, column=2)
    b_log.grid(row=2, column=3)
    b_sin.grid(row=3, column=3)
    b_cos.grid(row=4, column=3)
    b_tan.grid(row=5, column=3)
    return
def scilog():
                          logi=input.get()
                          input.delete(0,END)
                          l1=int(logi)
                          l2=math.log(l1,10)
                          input.insert(0,l2)

              
                                                                                
def nor():
		b_nor.grid_forget()
		b_log.grid_forget()
		b_sin.grid_forget()
		b_cos.grid_forget()
		b_tan.grid_forget()		
		return                          

def sin():
    sin=input.get()
    input.delete(0,END)
    s1=int(sin)
    s2=math.sin(s1)
    input.insert(0,s2)	
    return	
def cos():
                          cos=input.get()
                          input.delete(0,END)
                          c1=int(cos)
                          c2=math.cos(c1)
                          input.insert(0,c2)	
                          return
   	
def tan():
                          tan=input.get()
                          input.delete(0,END)
                          t1=int(tan)
                          t2=math.tan(t1)
                          input.insert(0,t2)	
                          return	

#creating button^s

#creating num button^s
b1 =Button(root,text="1", command=lambda:button(1), padx=50 ,pady=25,bg="black", fg="white")
b2 =Button(root,text="2", command=lambda:button(2), padx=50 ,pady=25,bg="black", fg="white")
b3 =Button(root,text="3", command=lambda:button(3), padx=50 ,pady=25,bg="black", fg="white")
b4 =Button(root,text="4", command=lambda:button(4), padx=50 ,pady=25,bg="black", fg="white")
b5 =Button(root,text="5", command=lambda:button(5), padx=50 ,pady=25,bg="black", fg="white")
b6 =Button(root,text="6", command=lambda:button(6), padx=50 ,pady=25,bg="black", fg="white")
b7 =Button(root,text="7", command=lambda:button(7), padx=50 ,pady=25,bg="black", fg="white")
b8 =Button(root,text="8", command=lambda:button(8), padx=50 ,pady=25,bg="black", fg="white")
b9 =Button(root,text="9", command=lambda:button(9), padx=50 ,pady=25,bg="black", fg="white")
b0 =Button(root,text="0", command=lambda:button(0), padx=50 ,pady=25,bg="black", fg="white")

#button^s of signs

b_add=Button(root,text="+", command=lambda:button("+"), padx=49,pady=25,bg="grey", fg="white")
b_sub=Button(root,text="-", command=lambda:button("-"), padx=50,pady=25,bg="grey", fg="white")
b_mul=Button(root,text="x", command=lambda:button("*"), padx=50,pady=25,bg="grey", fg="white")
b_div=Button(root,text="/", command=lambda:button("/"), padx=50,pady=25,bg="grey", fg="white")
b_mod=Button(root,text="%", command=lambda:button("%"), padx=48,pady=25,bg="grey", fg="white")
b_dot=Button(root,text=".", command=lambda:button("."), padx=50,pady=25,bg="grey", fg="white")

#scientific tools
b_sci=Button(root, text ="Sci", command=sci , padx=107, pady=25)

#execution button^s
b_clear=Button(root,text="C", command=clear, padx=110,pady=25, bg="red")
b_equal=Button(root,text="=", command=equal, padx=230,pady=25, bg="light green")

#mapping  button^s

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)

b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=5, column=1)

b_add.grid(row=2, column=3)
b_sub.grid(row=3, column=3)
b_mul.grid(row=4, column=3)
b_div.grid(row=5, column=3)
b_mod.grid(row=5, column=2)
b_dot.grid(row=5, column=0)

b_sci.grid(row=1, column = 0, columnspan=2)


b_clear.grid(row=1, column=2, columnspan=2)
b_equal.grid(row=6, column=0, columnspan=4)

#root_var loop

root.mainloop()