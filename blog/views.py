from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.shortcuts import render, get_object_or_404
from .models import Blog



@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.doctor = request.user   # current logged-in doctor
            blog.save()
            return redirect('my_blogs')  # doctor apne blogs dekh sakega
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})


@login_required
def my_blogs(request):
    blogs = request.user.blogs.all()  # doctor ke blogs
    return render(request, "blog/my_blogs.html", {"blogs": blogs})





# Patients: Blog List with category filter
def blog_list(request):
    category = request.GET.get("category")
    blogs = Blog.objects.filter(is_draft=False)  # sirf published

    if category:
        blogs = blogs.filter(category=category)

    categories = Blog._meta.get_field("category").choices

    return render(request, "blog/blog_list.html", {
        "blogs": blogs,
        "categories": categories,
        "selected_category": category,
    })

# Patients: Blog Detail
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk, is_draft=False)
    return render(request, "blog/blog_detail.html", {"blog": blog})


@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, doctor=request.user)

    if request.method == "POST":
        blog.delete()
        return redirect('my_blogs') 

    return render(request, 'blog/confirm_delete.html', {'blog': blog})