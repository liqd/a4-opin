from contrib.validations import image_validations


def validate_hero_image(image):
    image_validations.validate_image(image, 1300, 600)


def validate_logo(image):
    image_validations.validate_image(image, 400, 400)
