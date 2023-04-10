import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, RequestFactory
from django.urls import reverse
from ecm2434.models import Quiz, Question
import cv2
import pyzbar.pyzbar as pyzbar
from .views import scan_qr
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse
from leaderboard.models import Score
from .views import article_one

class ScanQRTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        Score.objects.filter(player=self.user).delete()
        Score.objects.create(player=self.user, score=0)
      

    def test_scan_qr_view_post_request(self):
        # Load the QR code image file
        with open('test_qr_code.png', 'rb') as img_file:
            # Create a SimpleUploadedFile object from the image file
            mock_image = SimpleUploadedFile('test_qr_code.png', img_file.read(), content_type='image/png')

            # Prepare the POST request with the image file
            request = self.factory.post(reverse('scan_qr'), {'image': mock_image})

            # Test the scan_qr view with the POST request
            response = scan_qr(request)

            # Check if the view successfully redirected to the URL encoded in the QR code
            self.assertEqual(response.status_code, 302)
            decoded_objects = pyzbar.decode(cv2.imread('test_qr_code.png'))  
            expected_url = decoded_objects[0].data.decode('utf-8')
            self.assertEqual(response.url, expected_url)


    def test_article_one_first_visit(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('article_one'))
        self.assertEqual(response.status_code, 200)

        # Check if the user's score is updated
        updated_score = Score.objects.get(player=self.user)
        self.assertEqual(updated_score.score, 10)

        # Check if the session variable 'visited_article_one' is set to True
        self.assertTrue(response.wsgi_request.session['visited_article_one'])
    

    def test_article_one_subsequent_visit(self):
        self.client.login(username='testuser', password='testpassword')

        # Update the user's initial score
        initial_score = Score.objects.get(player=self.user)
        initial_score.score = 10
        initial_score.save()

        # Set the session variable 'visited_article_one' to True
        session = self.client.session
        session['visited_article_one'] = True
        session.save()

        # Send a GET request to the article_one view
        response = self.client.get(reverse('article_one'))

        # Check if the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the user's score remains unchanged
        updated_score = Score.objects.get(player=self.user)
        self.assertEqual(updated_score.score, initial_score.score)

        # Check if the session variable 'visited_article_one' is still set to True
        self.assertTrue(response.wsgi_request.session['visited_article_one'])


