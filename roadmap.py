from manim import *
class roadmap(Scene):
    def construct(self):   
        a1 = VGroup(*[Arrow().scale(.9) for _ in range(3)]).arrange(UP,buff=1.2)
        l1 = Line(UP,DOWN).move_to(a1[0].get_start()).shift(UP*1.55).scale(1.56)
        l2 = Line().move_to(a1[1].get_start()).scale(1.5)
        all1 = VGroup(a1,l1,l2).scale(0.6).set_color('#717070FF')
        
        r1 = Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a1[2].get_end()).shift(RIGHT*1.22)
        t1 = Text('What is blockchain?', font= 'Monospace', font_size= 14).move_to(r1.get_center())
        r2 = r1.copy().move_to(a1[1].get_end()).shift(RIGHT*1.22)
        t2 = Text('How it works?', font= 'Monospace', font_size= 14).move_to(r2.get_center())
        r3 = Rectangle(height=0.7, width=2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a1[0].get_end()).shift(RIGHT*1.22)
        t3 = Text('why do we use', font= 'Monospace', font_size= 14).move_to(r3.get_center()).shift(UP*0.12)
        t4 = Text('Blockchain?', font= 'Monospace', font_size= 14).move_to(t3.get_center()).shift(DOWN*0.22)
        
        g1 = VGroup(all1, r1, t1, r2, t2, r3, t3, t4).scale(0.5).shift(UR*2.08 + RIGHT*2).shift(UP*0.1)
        
        a2 = VGroup(*[Arrow().scale(.9) for _ in range(3)]).arrange(UP,buff=0.8).rotate(-180* DEGREES).set_color('#717070FF')
        l3 = Line(UP,DOWN).move_to(a2[0].get_start()).shift(DOWN*1.14).scale(1.16).set_color('#717070FF')
        l4 = Line().move_to(a2[1].get_start()).scale(1.5).set_color('#717070FF')
        r4 = Rectangle(height=0.9, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a2[0].get_end()).shift(LEFT*1.27)
        r5 = Rectangle(height=0.7, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a2[1].get_end()).shift(LEFT*1.27)
        r6 = Rectangle(height=0.9, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a2[2].get_end()).shift(LEFT*1.27)
        t5 = Text('Learn about', font= 'Monospace', font_size= 14).move_to(r4.get_center()).shift(UP*0.15)
        t6 = Text('Distributed Ledger', font= 'Monospace', font_size= 14).move_to(r4.get_center()).shift(DOWN*0.17)
        t7 = Text('Learn Basics of', font= 'Monospace', font_size= 14).move_to(r5.get_center()).shift(UP*0.12)
        t8 = Text('Crptography', font= 'Monospace', font_size= 14).move_to(r5.get_center()).shift(DOWN*0.15)
        t9 = Text('Differences', font= 'Monospace', font_size= 14).move_to(r6.get_center()).shift(UP*0.25)
        t10 = Text('between Web1', font= 'Monospace', font_size= 14).move_to(r6.get_center()).shift(UP*0.001)
        t11 = Text('Web2 and Web3', font= 'Monospace', font_size= 14).move_to(r6.get_center()).shift(DOWN*0.25)
        
        g2 = VGroup(a2, l3, l4, r4, r5, r6, t5, t6, t7, t8, t9,t10, t11).scale(0.5).shift(UL*2 + LEFT*2).shift(UP*0.1)
        
        r7 = Rectangle(height=2, width= 4.5).set_color('#717070FF')
        t12 = Text('choose any programming language', font= 'Monospace', font_size= 14).move_to(r7.get_center()).shift(UP*0.75)
        r8 = Rectangle(height=0.5, width= 1.5,fill_opacity=1,fill_color='#7F6D2CFF', stroke_color= '#3E3C3B00')
        t13 = Text('Solidity', font= 'Monospace', font_size= 14).move_to(r8.get_center())
        gg1 = VGroup(r8, t13).move_to(r7).shift(LEFT*1 + UP*0.22)
        r9 =  Rectangle(height=0.5, width= 1.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(r7).shift(RIGHT*1 + UP* 0.22)
        t14 = Text('Rust', font= 'Monospace', font_size= 14).move_to(r9.get_center())
        r10 =  Rectangle(height=0.5, width= 1.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(r7,DOWN).shift(RIGHT*1 + UP* 0.3)
        t15 = Text('Vyper', font= 'Monospace', font_size= 14).move_to(r10.get_center())
        r11 =  Rectangle(height=0.5, width= 1.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(r7,DOWN).shift(LEFT*1 + UP* 0.3)
        t16 = Text('Javascript', font= 'Monospace', font_size= 14).move_to(r11.get_center())
       
        gg3 = VGroup(r7,t12,gg1,r9,t14,r10,t15,r11,t16)
        ar1 = Arrow(stroke_width=5,max_tip_length_to_length_ratio=0.15).move_to(gg3).shift(LEFT*4.65).scale(3.2).set_color('#717070FF')
        g3 = VGroup(gg3, ar1).scale(0.5).next_to(g1, DOWN*1.8).shift(RIGHT*0.1)
        
        a3 = VGroup(*[Arrow().scale(.9) for _ in range(3)]).arrange(UP,buff=0.9).rotate(-180*DEGREES).set_color('#717070FF')
        l5 = Line(UP,DOWN).move_to(a3[2].get_start()).shift(UP*1.25).scale(1.26).set_color('#717070FF')
        l6 = Line().move_to(a3[1].get_start()).scale(1.1).set_color('#717070FF')
        r12 = Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a3[0].get_end()).shift(LEFT*1.27)
        r13 = Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a3[1].get_end()).shift(LEFT*1.27)
        r14 = Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a3[2].get_end()).shift(LEFT*1.27)
        t17 = Text('Learn Basic Syntax', font= 'Monospace', font_size= 14).move_to(r12.get_center())
        t18 = Text('Remix IDE', font= 'Monospace', font_size= 14).move_to(r13.get_center())
        t19 = Text('Build Project', font= 'Monospace', font_size= 14).move_to(r14.get_center())
        
        g4 = VGroup(a3,l5,l6,r12,r13,r14,t17,t18,t19).scale(0.5).shift(LEFT*4, DOWN)
        
        a4 = VGroup(*[Arrow().scale(.9) for _ in range(2)]).arrange(UP,buff=0.8).rotate(-180*DEGREES).set_color('#717070FF')
        l7= Line(UP,DOWN).move_to(a4[1].get_start()).shift(UP*0.57).scale(0.6).set_color('#717070FF')
        l8 = Line().move_to(l7.get_center()).scale(0.5).shift(RIGHT*0.48).set_color('#717070FF')
        r15= Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a4[0].get_end()).shift(LEFT*1.27)
        r16= Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a4[1].get_end()).shift(LEFT*1.27)
        t20 = Text('IPFS', font= 'Monospace', font_size= 14).move_to(r15.get_center())
        t21 = Text('SWARM', font= 'Monospace', font_size= 14).move_to(r16.get_center())
        
        g5 = VGroup(a4,l7,l8,r15,r16,t20,t21).scale(0.5).next_to(g4, DOWN*2.5).shift(RIGHT*0.22)
        
        a5 = VGroup(*[Arrow().scale(.9) for _ in range(2)]).arrange(UP,buff=0.8).set_color('#717070FF')
        l9= Line(UP,DOWN).move_to(a5[1].get_start()).shift(DOWN*0.57).scale(0.6).set_color('#717070FF')
        l10 = Line().move_to(l9.get_center()).scale(1.5).shift(LEFT*1.5).set_color('#717070FF')
        r17= Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a5[0].get_start()).shift(RIGHT*2.55)
        r18= Rectangle(height=0.5, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a5[1].get_start()).shift(RIGHT*2.55)
        t22 = Text('Web3.js', font= 'Monospace', font_size= 14).move_to(r17.get_center())
        t23 = Text('Ether.js', font= 'Monospace', font_size= 14).move_to(r18.get_center())
        
        g6 = VGroup(a5,l9,l10,r17,r18,t22,t23).scale(0.5).next_to(g3, DOWN*2.5).shift(RIGHT*0.22)
        
        a6 = VGroup(*[Arrow().scale(.9) for _ in range(2)]).arrange(UP,buff=0.8).set_color('#717070FF')
        l11= Line(UP,DOWN).move_to(a6[1].get_start()).shift(DOWN*0.57).scale(0.6).set_color('#717070FF')
        l12 = Line().move_to(l11.get_center()).scale(0.5).shift(LEFT*0.48).set_color('#717070FF')
        r19= Rectangle(height=0.9, width= 2.5,fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a6[0].get_start()).shift(RIGHT*2.55)
        r20= Rectangle(height=0.5, width= 2.5, fill_opacity=1,color='#7F6D2CFF', stroke_color= '#3E3C3B00').move_to(a6[1].get_start()).shift(RIGHT*2.55)
        t24 = Text('Truffle and', font= 'Monospace', font_size= 14).move_to(r19.get_center()).shift(UP*0.12)
        t25 = Text('Ganache', font= 'Monospace', font_size= 14).move_to(r19.get_center()).shift(DOWN* 0.15)
        t26 = Text('HardHat', font= 'Monospace', font_size= 14).move_to(r20.get_center())
        
        g7 = VGroup(a6,l11,l12,r19,r20,t24,t25,t26).scale(0.5).next_to(g6, DOWN*1.6).shift(RIGHT*0.05)
        
        
        r21 = Rectangle(height=2, width= 4.5, fill_opacity=1, fill_color='#D7A6EA00', stroke_color='#9904F000')
        t27 = Text('BLOCKCHAIN', font= 'Monospace', font_size= 24).move_to(r21.get_center()).shift(UP*0.12).set_color('#0000000')
        t28 = Text('DEVELOPER ROADMAP', font= 'Monospace', font_size= 24).move_to(r21.get_center()).shift(DOWN*0.25).set_color('#0000000')
        
        g8 = VGroup(r21, t27, t28).move_to(UP*3.5).scale(0.4)
        
        ar2 = Arrow(UP, DOWN,stroke_width=0.8, max_tip_length_to_length_ratio=0.15).next_to(g8, DOWN).scale(0.3).shift(UP*0.8).set_color('#717070FF')
        r22= Rectangle(height=0.6, width= 2,fill_opacity=1, fill_color='#FDF36500', stroke_color='#2D2D2D00').move_to(ar2.get_end()).shift(DOWN*0.18)
        t29 = Text('BLOCKCHAIN', font= 'Monospace', font_size= 18).move_to(r22.get_center()).set_color('#0000000')
        var1 = VGroup(r22, t29).scale(0.55)
        
        ar3 = Arrow(UP, DOWN,stroke_width=0.8, max_tip_length_to_length_ratio=0.15).next_to(r22, DOWN).scale(0.4).shift(UP*0.7).set_color('#717070FF')
        r23= Rectangle(height=0.8, width= 2, fill_opacity=1,fill_color='#FDF36500', stroke_color='#2D2D2D00').move_to(ar3.get_end()).shift(DOWN*0.23)
        t30 = Text('SMART', font= 'Monospace', font_size= 18).move_to(r23.get_center()).shift(UP*0.12).set_color('#0000000')
        t31 = Text('CONTRACT', font= 'Monospace', font_size= 18).move_to(r23.get_center()).shift(DOWN*0.15).set_color('#0000000')
        var2 = VGroup(r23, t30, t31).scale(0.55)
        
        ar4 = Arrow(UP, DOWN,stroke_width=0.8, max_tip_length_to_length_ratio=0.15).next_to(r23, DOWN).scale(0.4).shift(UP*0.7).set_color('#717070FF')
        r24= Rectangle(height=0.6, width= 2, fill_opacity=1,fill_color='#FDF36500', stroke_color='#2D2D2D00').move_to(ar4.get_end()).shift(DOWN*0.18)
        t32 = Text('SOLIDITY', font= 'Monospace', font_size= 18).move_to(r24.get_center()).set_color('#0000000')
        var3 = VGroup(r24, t32).scale(0.55)
        
        ar5 = Arrow(UP, DOWN,stroke_width=0.8, max_tip_length_to_length_ratio=0.15).next_to(r24, DOWN).scale(0.4).shift(UP*0.7).set_color('#717070FF')
        r25= Rectangle(height=0.6, width= 2, fill_opacity=1,fill_color='#FDF36500', stroke_color='#2D2D2D00').move_to(ar5.get_end()).shift(DOWN*0.18)
        t33 = Text('D-APPS', font= 'Monospace', font_size= 18).move_to(r25.get_center()).set_color('#0000000')
        var4 = VGroup(r25, t33).scale(0.55)
        
        ar6 = Arrow(UP, DOWN,stroke_width=0.8, max_tip_length_to_length_ratio=0.15).next_to(r25, DOWN).scale(0.4).shift(UP*0.7).set_color('#717070FF')
        r26= Rectangle(height=0.6, width= 2,fill_opacity=1, fill_color='#FDF36500', stroke_color='#2D2D2D00').move_to(ar6.get_end()).shift(DOWN*0.18)
        t34 = Text('FRAMEWORKS', font= 'Monospace', font_size= 18).move_to(r26.get_center()).set_color('#0000000')
        var5 = VGroup(r26, t34).scale(0.55)
        
        ar7 = Arrow(UP, DOWN,stroke_width=0.8, max_tip_length_to_length_ratio=0.15).next_to(r26, DOWN).scale(0.4).shift(UP*0.7).set_color('#717070FF')
        r27= Rectangle(height=0.8, width= 2, fill_opacity=1,fill_color='#FDF36500', stroke_color='#2D2D2D00').move_to(ar7.get_end()).shift(DOWN*0.22)
        t35 = Text('DISTRIBUTED', font= 'Monospace', font_size= 18).move_to(r27.get_center()).shift(UP*0.12).set_color('#0000000')
        t36 = Text('STORAGE', font= 'Monospace', font_size= 18).move_to(r27.get_center()).shift(DOWN*0.15).set_color('#0000000')
        
        var6 = VGroup(r27, t35,t36).scale(0.55)
        
        
        ar8 = Arrow(UP, DOWN,stroke_width=0.8, max_tip_length_to_length_ratio=0.15).next_to(r27, DOWN).scale(0.5).shift(UP*0.7).set_color('#717070FF')
        r28= Rectangle(height=0.6, width= 4.5, fill_opacity=1, fill_color='#D7A6EA00', stroke_color='#F8F2FF00').move_to(ar8.get_end()).shift(DOWN*0.18)
        t37 = Text('Go on and Build Projects', font= 'Monospace', font_size= 18).move_to(r28.get_center()).set_color('#0000000')
        
        var7 = VGroup(r28, t37).scale(0.55)
        
        
        self.play(
            Write(g1),
            Write(g2),
            Write(g3),
            Write(g4),
            Write(g5),
            Write(g6),
            Write(g7), run_time = 1.2 
        )
        self.wait(2)
        self.play(GrowFromCenter(g8), run_time = 0.15)
        self.play(GrowFromCenter(ar2),  run_time = 0.15)
        self.play(GrowFromCenter(var1), run_time = 0.15)
        self.play(GrowFromCenter(ar3), run_time = 0.15)
        self.play(GrowFromCenter(var2), run_time = 0.15)
        self.play(GrowFromCenter(ar4), run_time = 0.15)
        self.play(GrowFromCenter(var3), run_time = 0.15)
        self.play(GrowFromCenter(ar5), run_time = 0.15)
        self.play(GrowFromCenter(var4), run_time = 0.15)
        self.play(GrowFromCenter(ar6), run_time = 0.15)
        self.play(GrowFromCenter(var5), run_time = 0.15)
        self.play(GrowFromCenter(ar7), run_time = 0.15)
        self.play(GrowFromCenter(var6), run_time = 0.15)
        self.play(GrowFromCenter(ar8), run_time = 0.15)
        self.play(GrowFromCenter(var7), run_time = 0.15)
        
        self.play(
            g1.animate.next_to(var1, RIGHT*0.1).shift(LEFT*0.05),
            g2.animate.next_to(var1, LEFT*0.1).shift(RIGHT*0.05), run_time = 0.15
            
        )
        
        
        
            
            
        self.play(
            g3.animate.next_to(var2, RIGHT*0.1).shift(LEFT*0.05),run_time = 0.15
            
        )
        self.play(
            g4.animate.next_to(var3, LEFT*0.1).shift(RIGHT*0.05),run_time = 0.15
            
        )
        
        
        self.play(
            g6.animate.next_to(var4, RIGHT*0.1).shift(LEFT*0.05),run_time = 0.15
            
        )
        
        self.play(
            g7.animate.next_to(var5, RIGHT*0.1).shift(LEFT*0.05),run_time = 0.15
            
        )
        
        self.play(
            g5.animate.next_to(var6, LEFT*0.1).shift(RIGHT*0.05),run_time = 0.15
            
        )
        
        self.wait(3)
        
       
    
        

        