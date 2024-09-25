from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a smaller name"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     ratings = forms.IntegerField(label="Your Ratings", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = "__all__"  # ['column_name_to_be_included']
        # exclude = ['column_name_to_hide'] 
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages={
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a smaller name"
                }
            }
