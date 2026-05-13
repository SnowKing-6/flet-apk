import flet as ft

async def main(page: ft.Page):
    page.title = "Razi Tasbeeh"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLACK
    page.rtl = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    ACCENT = ft.colors.CYAN_700
    count = 0
    records = []

    number_text = ft.Text(value="0", size=50, weight="bold", color="white")
    progress_ring = ft.ProgressRing(
        value=0, stroke_width=8, color=ACCENT, bgcolor=ft.colors.GREY_900,
        width=200, height=200
    )
    records_list = ft.ListView(expand=True, spacing=10, padding=20)

    def increment(e):
        nonlocal count
        count += 1
        number_text.value = str(count)
        progress_ring.value = (count % 101) / 100
        page.update()

    def save_record(e):
        if count > 0:
            records.append(count)
            records_list.controls.insert(0, ft.Container(
                content=ft.Row([
                    ft.Text(f"التسجيل #{len(records)}", weight="bold", color=ACCENT),
                    ft.Text(f"العدد: {count}", color="white"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=10, bgcolor=ft.colors.GREY_900, border_radius=10
            ))
            page.update()

    page.add(
        ft.Column([
            ft.Text("المسبحة الإلكترونية", size=24, color=ACCENT, weight="bold"),
            ft.Stack([progress_ring, ft.Container(content=number_text, alignment=ft.alignment.center, width=200, height=200)]),
            ft.ElevatedButton("سبح", icon=ft.icons.ADD, on_click=increment, width=200, height=60, bgcolor=ACCENT, color="white"),
            ft.TextButton("سجل النتيجة", icon=ft.icons.SAVE, on_click=save_record),
            ft.Container(content=records_list, height=200, width=300, border=ft.border.all(1, ft.colors.GREY_800), border_radius=15)
        ], horizontal_alignment="center")
    )

if __name__ == "__main__":
    ft.app(target=main)
