from django import forms
from inventory.models import Category, Brand, Item, System, SystemComponent, Archive

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'brand', 'total_count']  # Include necessary fields

class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['system_name', 'status']

class SystemComponentForm(forms.ModelForm):
    class Meta:
        model = SystemComponent
        fields = ['component_item', 'component_type', 'serial_number']  # Updated field

class SystemComponentArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = ['archive_type', 'remark']