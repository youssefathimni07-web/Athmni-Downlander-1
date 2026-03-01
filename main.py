import flet as ft
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    all_chars = ""
    if use_upper:
        all_chars += string.ascii_uppercase
    if use_lower:
        all_chars += string.ascii_lowercase
    if use_digits:
        all_chars += string.digits
    if use_symbols:
        all_chars += string.punctuation

    if not all_chars:
        return "اختر على الأقل نوع واحد من الأحرف!"

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main(page: ft.Page):
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    password_text = ft.Text(value="", size=20, selectable=True)

    # مدخل طول الباسورد
    length_input = ft.TextField(label="طول كلمة المرور", value="16", width=200)

    # خيارات الباسورد
    upper_cb = ft.Checkbox(label="أحرف كبيرة", value=True)
    lower_cb = ft.Checkbox(label="أحرف صغيرة", value=True)
    digits_cb = ft.Checkbox(label="أرقام", value=True)
    symbols_cb = ft.Checkbox(label="رموز خاصة", value=True)

    def generate_click(e):
        try:
            length = int(length_input.value)
            password = generate_password(
                length,
                upper_cb.value,
                lower_cb.value,
                digits_cb.value,
                symbols_cb.value
            )
            password_text.value = password
            page.update()
        except:
            password_text.value = "أدخل طول صحيح!"
            page.update()

    generate_button = ft.ElevatedButton("توليد كلمة مرور", on_click=generate_click)

    page.add(
        ft.Column([
            length_input,
            upper_cb,
            lower_cb,
            digits_cb,
            symbols_cb,
            generate_button,
            password_text
        ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
