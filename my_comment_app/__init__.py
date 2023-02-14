def get_model():
    from my_comment_app.models import CustomizedComment
    return CustomizedComment

def get_form():
    from my_comment_app.forms import CustomizedCommentForm
    return CustomizedCommentForm