import flet as ft

def main(page: ft.Page):
    def handle_add_task(e):
        # ADD NEW TASK EVENT HANDLER
        tasks_viewport.controls.append(ft.Checkbox(label=new_task_input.value))
        new_task_input.value = ""
        viewport.update()

    new_task_input = ft.TextField(hint_text="Whats needs to be done?", on_submit=handle_add_task)
    tasks_viewport = ft.Column()

    viewport = ft.Column(
        width=600, 
        controls=[
            ft.Row(
                controls=[
                            new_task_input, 
                            ft.FloatingActionButton(
                                icon=ft.icons.ADD,
                                on_click=handle_add_task, 
                            )
                        ]
                    ), 
                    tasks_viewport,
                ]
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.add(viewport)



if __name__ =="__main__":
    ft.app(target=main)