from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'cedula', 'phone', 'career', 'email', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white outline-none', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white outline-none', 'placeholder': 'Last Name'}),
            'cedula': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white outline-none', 'placeholder': 'Cédula'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white outline-none', 'placeholder': 'Phone Number'}),
            'career': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white outline-none', 'placeholder': 'Career'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white outline-none', 'placeholder': 'Email'}),
            'photo': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white outline-none'}),
        }
