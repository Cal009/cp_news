from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm


class LikeView(LoginRequiredMixin, View):
    """
    A view to allow users to like a post

    Gets the information of the post and the user.

    If user has already liked then like will be removed if clicked again

    If not then like will be added to like count

    User will be redirected to the same post for good UX

    For both likes and dislikes they work in tandem making it so users cannot 
    click both buttons, if one is already cliked it will remove the previous 
    choice and apply it to the new one
    """
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        user = request.user

        # Toggle like
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)  # Remove the like
        else:
            post.dislikes.remove(user)  # Remove the dislike if it exists
            post.likes.add(user)  # Add like

        return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))


class DisLikeView(LoginRequiredMixin, View):
    """
    A view to allow users to dislike a post

    Gets the information of the post and the user.

    If user has already disliked then dislike will be removed if clicked again

    If not then dislike will be added to dislike count

    User will be redirected to the same post for good UX

    For both likes and dislikes they work in tandem making it so users cannot 
    click both buttons, if one is already cliked it will remove the previous 
    choice and apply it to the new one
    """
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        user = request.user

        # Toggle dislike
        if post.dislikes.filter(id=user.id).exists():
            post.dislikes.remove(user)  # Remove the dislike
        else:
            post.likes.remove(user)  # Remove the like if it exists
            post.dislikes.add(user)  # Add dislike

        return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "news/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/login/")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
                )

    total_likes = post.total_likes()

    return render(
        request,
        "news/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "total_likes": total_likes,
        }
    )


def comment_edit(LoginRequiredMixin, request, slug, comment_id):
    """
    View to edit comments

    Gives the ability for a logged in user to leave a comment

    Will not show if the user is not logged in

    Error messages in place incase comment isnt correctly updated
    """
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/login/")

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(LoginRequiredMixin, request, slug, comment_id):
    """
    view to delete comment

    Gives ability for creator of the comment to delete it

    Does not allow other users to delete other comments

    Provides feedback to user for good UX
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
