import flet as ft
import time

def main(page: ft.Page):

    page.title = "Photo Frame Project"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()
     
    img1 = ft.Image(
        src=f"https://picsum.photos/800/400?0",
        width=800,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10),
    )

    img2 = ft.Image(
        src=f"https://picsum.photos/800/400?1",
        width=800,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10),
    )

    img3 = ft.Image(
        src=f"https://picsum.photos/800/400?2",
        width=800,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10)
    )

    img4 = ft.Image(
        src=f"https://picsum.photos/800/400?3",
        width=800,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10)
    )

    img5 = ft.Image(
        src=f"https://picsum.photos/800/400?1",
        width=800,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10)
    )

    img = ft.AnimatedSwitcher(
        img1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    autoplay = True

    def nextpic(e):
        global autoplay
        autoplay = False

        if img.content == img1:
            img.content = img2
        elif img.content == img2:
            img.content = img3
        elif img.content == img3:
            img.content = img4
        elif img.content == img4:
            img.content = img5
        else:
            img.content = img1
        img.update()

    def prevtpic(e):
        global autoplay
        autoplay = False

        if img.content == img5:
            img.content = img4
        elif img.content == img4:
            img.content = img3
        elif img.content == img3:
            img.content = img2
        elif img.content == img2:
            img.content = img1
        else:
            img.content = img5
        img.update()

    def autoplay(e):
        global autoplay
        autoplay = True
        while autoplay == True:
            if img.content == img1:
                img.content = img2
            elif img.content == img2:
                img.content = img3
            elif img.content == img3:
                img.content = img4
            elif img.content == img4:
                img.content = img5
            else:
                img.content = img1
            img.update()
            time.sleep(3)


    page.add(
        ft.Column([
            ft.Text("Digital Photo Frame", size=24),
        ]),
        ft.Column([
            ft.Text("Helen Peña 12-II", size=12),
        ]), 
        ft.Column([
            ft.Row(
            [
                ft.IconButton(ft.icons.NAVIGATE_BEFORE, on_click=prevtpic), 
                ft.Container(
                    img, 
                    width=800, 
                    height=400, 
                    border_radius=ft.border.all(20)
                ),
                ft.IconButton(ft.icons.NAVIGATE_NEXT, on_click=nextpic),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            
            ),

            ft.Row([
                ft.IconButton(ft.icons.PLAY_ARROW, on_click=autoplay),
                ft.Text(" Click to autoplay", size=12)
            ],
            alignment=ft.MainAxisAlignment.CENTER,),
            
        ],
        scroll=ft.ScrollMode.ALWAYS,) 
    ),

ft.app(target=main)

#For web display
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)