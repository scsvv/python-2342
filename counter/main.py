import flet as ft 

def main(page: ft.Page):
    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    number_input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_in = ft.TextField(value="10", text_align=ft.TextAlign.RIGHT, width=100)
    
    def minus_click(event):
        number_input.value = str(int(number_input.value) - 1)
        page.update()
    
    def plus_click(event):
        number_input.value = str(int(number_input.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [   
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click, width=80), 
                number_input, 
                ft.IconButton(ft.icons.ADD, on_click=plus_click, width=80), 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [   
                ft.TextButton("Remove", width=80),
                txt_in, 
                ft.TextButton("Add", width=80) 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ) 

    )



if __name__ == "__main__":
    ft.app(target=main)