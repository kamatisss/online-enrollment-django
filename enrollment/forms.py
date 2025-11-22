from django import forms
from django.core.validators import MinValueValidator, RegexValidator
from student_list.models import Personal_Background, Education_Background,Family_Background,Course, Tuition


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal_Background
        fields = ['name','age','gender','address','email']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        if not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError("Name should only contain letters and spaces.")
        return name
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        try:
            age = int(age)
        except (TypeError, ValueError):
            raise forms.ValidationError("Age must be a number.")
        
        if age < 1 or age > 120:
            raise forms.ValidationError("Age must be between 1 and 120.")
        return age


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education_Background
        fields = ['education_level','school_name','school_address','course','year']

    def clean_year(self):
        year = self.cleaned_data.get('year')
        try:
            year = int(year)
        except (TypeError, ValueError):
            raise forms.ValidationError("Year must be a number.")
        if year < 1900 or year > 2100:
            raise forms.ValidationError("Enter a valid year.")
        return year


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family_Background
        fields = ['father_name','mother_name','number_of_siblings','guardian_name','guardian_contact']

    def clean_number_of_siblings(self):
        siblings = self.cleaned_data.get('number_of_siblings')

        try:
            siblings = int(siblings)
        except (TypeError, ValueError):
            raise forms.ValidationError("Invalid number.")

        if siblings < 0:
            raise forms.ValidationError("Number of siblings cannot be negative.")

        return siblings


    def clean_guardian_contact(self):
        contact = self.cleaned_data.get('guardian_contact')
        if not contact.isdigit() or len(contact) < 10:
            raise forms.ValidationError("Enter a valid phone number with at least 10 digits.")
        return contact

class TuitionForm(forms.ModelForm):
    class Meta:
        model = Tuition
        fields = ['payment_id','course_id','semester','amount','Due_date']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        # Convert to integer (or float if needed)
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise forms.ValidationError("Amount must be a valid number.")

        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")

        return amount


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id','course_code','course_name','department','units']

    def clean_units(self):
        units = self.cleaned_data.get('units')

        # Convert to integer safely
        try:
            units = int(units)
        except (TypeError, ValueError):
            raise forms.ValidationError("Units must be a valid number.")

        if units < 1:
            raise forms.ValidationError("Units cannot be less than 1.")

        return units


    def clean_course_code(self):
        code = self.cleaned_data.get('course_code').upper()
        if not code.isalnum():
            raise forms.ValidationError("Course code must contain only letters and numbers.")
        return code

        
