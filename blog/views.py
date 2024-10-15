from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from blog.models import Contact
from .forms import ResumeSubmissionForm
import yagmail

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')  # Ensure this is captured from the form

        # Check if name and message are provided
        if name and message:  
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
        else:
            messages.error(request, 'Name and message fields cannot be empty.')

    return render(request, 'home.html')


def submit_resume(request):
    if request.method == 'POST':
        form = ResumeSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Fetch data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            resume = request.FILES['resume']

            try:
                # Initialize Yagmail SMTP connection
                yag = yagmail.SMTP(settings.EMAIL_HOST_USER)

                # Prepare email content
                subject = f'New Resume Submission from {name}'
                body = f'You have received a new resume submission from {name} ({email}).'

                # Send email with resume attachment
                yag.send(
                    to='anishagazi29@gmail.com',  # Example recipient email
                    subject=subject,
                    contents=body,
                    attachments=resume.file  # Attach the resume file directly
                )

                messages.success(request, 'Your resume has been submitted and emailed successfully!')
                return redirect('home')

            except Exception as e:
                # Handle any email sending errors
                messages.error(request, f'Failed to send the resume via email. Error: {str(e)}')
        else:
            messages.error(request, 'There was an error submitting your resume. Please try again.')
    else:
        form = ResumeSubmissionForm()
    
    return render(request, 'home.html', {'form': form})

def healthcare_page(request):
    return render(request, 'healthcare.html')

def finance_page(request):
    return render(request, 'finance.html')

def insurance_page(request):
    return render(request, 'insurance.html')
