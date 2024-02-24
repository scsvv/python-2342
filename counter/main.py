import flet as ft 

def main(page: ft.Page):
    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    number_input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_in = ft.TextField(value="10", text_align=ft.TextAlign.RIGHT, width=100)
    
    def minus(basis, decrement):
        return basis - decrement
    
    def plus(basis, increment):
        return basis + increment

    def handle_click(event):
        try:
            data = int(number_input.value)
            increment = int(txt_in.value)
        except ValueError:
            number_input.value = str(0)
            increment.value = str(10)
            page.update()
            return
        
        result = {
            1: minus(data, 1),
            2: plus(data, 1),
            3: minus(data, increment),
            4: plus(data, increment),
        }.get(event.control.data, data)
        
        number_input.value = str(result)
        page.update()



    page.add(
        ft.Row(
            [   
                ft.IconButton(ft.icons.REMOVE, on_click=handle_click, width=80, data=1), 
                number_input, 
                ft.IconButton(ft.icons.ADD, on_click=handle_click, width=80, data=2), 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [   
                ft.TextButton("Remove",  on_click=handle_click, width=80, data=3),
                txt_in, 
                ft.TextButton("Add",  on_click=handle_click, width=80, data=4) 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ) 

    )

if __name__ == "__main__":
    ft.app(target=main)