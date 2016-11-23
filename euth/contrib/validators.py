from contrib.validations import image_validations


def validate_hero_image(image):
    image_validations.validate_image(image, 1300, 600)


def validate_avatar(image):
    image_validations.validate_image(image, 200, 200)


def validate_logo(image):
    image_validations.validate_image(image, 200, 200, aspect_ratio=(1, 1))


def validate_idea_image(image):
    image_validations.validate_image(image, 800, 200)
