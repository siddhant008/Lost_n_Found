from django.shortcuts import render
from register.models import Register
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import face_recognition as fr


# Create your views here.
@login_required
def search(request):
    query = request.GET.get("q")
    if query:
        registers = Register.objects.filter(
            Q(name_lost__icontains=query)
        ).distinct()
        return render(request, 'search/search.html', {'registers': registers, 'request': request})
    else:
        registers = Register.objects.all()
        return render(request, 'search/search.html', {'registers': registers, 'request': request})


@login_required
def advanced_search(request):
    if request.method == 'POST' and request.FILES['unknown']:
        myfile = request.FILES['unknown']

        unknown_image = fr.load_image_file(myfile)
        unknown_face_encoding = fr.face_encodings(unknown_image)[0]
        known_images = []
        for obj in Register.objects.all():
            known_images.append(obj)
        ans = []
        for img in known_images:
            known_picture = fr.load_image_file(img.image_lost.path)
            known_face_encoding = fr.face_encodings(known_picture)[0]
            result = fr.compare_faces([known_face_encoding], unknown_face_encoding)
            if result[0]:
                ans.append(img)
                print("matched with ", img.name_lost)
        print(ans)
        return render(request, 'search/advanced_search.html', {'myfile': myfile, 'ans': ans, 'request': request})
    return render(request, 'search/advanced_search.html', {'request': request})

@login_required
def all_search(request):
    registers2 = Register.objects.all()
    return render(request, 'search/all_search.html', {'registers2': registers2, 'request': request})
