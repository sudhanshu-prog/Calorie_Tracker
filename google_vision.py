def analyze_food_image(image_file):
    try:
        client = vision.ImageAnnotatorClient() # type: ignore
        image = vision.Image(content=image_file.read()) # type: ignore
        response = client.label_detection(image=image)
        labels = [label.description for label in response.label_annotations]
        return labels
    except Exception as e:
        print(f"Error analyzing image: {e}")
        return []
