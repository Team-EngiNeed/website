from django.shortcuts import render, redirect
from .models import ContactMessage, Submission
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_object_or_404
from django.utils import timezone

def index(request):
  return render(request, 'index.html')

def about(request):
    if request.method == "POST":
        # Retrieve form data from the POST request
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Check if the required fields are not empty
        if full_name and email and message:
            # Save the form data to the ContactMessage model
            contact_message = ContactMessage(
                full_name=full_name,
                email=email,
                message=message
            )
            contact_message.save()  # Save the contact message to the database
            return redirect("engineed:about")  # Redirect back to the about page

    return render(request, "about.html")


def researchers(request):
  return render(request, 'researchers.html')



@login_required(login_url="/users/login/")
def index_new(request):
    return render(request, 'index_new.html')


@login_required(login_url="/users/login/")
def ticket(request):
    form = forms.Ticket()  # Initialize the form for GET requests

    if request.method == "POST":
        form = forms.Ticket(request.POST, request.FILES)  # Handle POST and file data

        if form.is_valid():
            # Save the form data but don't commit to the database yet
            new_ticket = form.save(commit=False)

            # Manually set the user as the author
            new_ticket.author = request.user

            # Handle dateSubmitted manually if necessary
            if 'dateSubmitted' in request.POST:
                new_ticket.dateSubmitted = timezone.make_aware(timezone.datetime.strptime(request.POST['dateSubmitted'], '%Y-%m-%dT%H:%M'))

            # Save the new ticket to the database
            new_ticket.save()

            # Redirect based on user role
            user_role = request.user.groups.values_list('name', flat=True)  # Assuming roles are assigned via groups
            if 'ENGINEED-ADMIN' in user_role or 'PRESIDENT' in user_role:
                return redirect('engineed:index_new')  # Redirect to engieed_index_new
            elif 'ENGINEER' in user_role:
                return redirect('engineed:engineer')  # Redirect to engineed:engineer
            elif 'ADVISER' in user_role:
                return redirect('engineed:adviser')  # Redirect to engineed:adviser
            else:
                return redirect('engineed:index')  # Default redirect

    return render(request, 'ticket.html', {'form': form})


@login_required(login_url="/users/login/")
def page(request):
    submissions = Submission.objects.all()  # Fetch updated submissions from the database
    return render(request, 'page.html', {'submissions': submissions})

@login_required
def order_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)

    # Check if the user is "VCSMS-Engineer" or the author of the submission
    can_edit = request.user.username == "VCSMS-Engineer" or request.user == submission.author

    if request.method == 'POST' and can_edit:
        # Update fields from form data
        submission.fullName = request.POST.get('fullName', submission.fullName)
        submission.gradeSection = request.POST.get('gradeSection', submission.gradeSection)
        submission.damagedProperty = request.POST.get('damagedProperty', submission.damagedProperty)
        submission.comment = request.POST.get('comment', submission.comment)
        submission.completed = 'completed' in request.POST
        submission.save()

        # Redirect based on user role
        user_role = request.user.groups.values_list('name', flat=True)  # Get user roles (assuming groups)
        if 'ENGINEED-ADMIN' in user_role or 'PRESIDENT' in user_role:
            return redirect('engineed:index_new')  # Redirect to engieed_index_new
        elif 'ENGINEER' in user_role:
            return redirect('engineed:engineer')  # Redirect to engineed:engineer
        elif 'ADVISER' in user_role:
            return redirect('engineed:adviser')  # Redirect to engineed:adviser
        else:
            return redirect('engineed:index')  # Default redirect

    return render(request, 'order.html', {
        'submission': submission,
        'username': request.user.username,
        'can_edit': can_edit
    })


@login_required
def adviser(request):
    # Extract the adviser's "group" by splitting at '-'
    adviser_username = request.user.username
    group_name, role = adviser_username.split('-')

    # Check if the logged-in user is an adviser
    if role.upper() != "ADVISER":
        return render(request, 'index.html')  # Redirect if not an adviser

    # Filter submissions where the author's username starts with the same group name
    # and sort by 'dateSubmitted' in descending order
    submissions = Submission.objects.filter(author__username__startswith=group_name).order_by('-dateSubmitted')

    # Check if submissions are correctly loaded
    if not submissions:
        print(f"No submissions found for group {group_name} (expected author username starting with '{group_name}')")

    # Pass the group name to the template
    return render(request, 'adviser.html', {'submissions': submissions, 'group_name': group_name})


@login_required
def engineer(request):
    # Retrieve all submissions, sorted from newest to oldest
    submissions = Submission.objects.all().order_by('-dateSubmitted')
    return render(request, 'engineer.html', {'submissions': submissions})