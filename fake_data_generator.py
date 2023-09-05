from random import randint, uniform
from datetime import datetime, timedelta

open("data.json", "w").close()  # for clearing json file if it exist
fp = open("data.json", "w")


def description(brand, subBrand, version):
    result = descriptionTemplate.format(
        brand=brands[brand],
        subBrand=subBrands[brand][subBrand],
        version=version,
        category=categories[brand][subBrand],
    )
    return result


def date_generator(start, end):
    date = start + timedelta(seconds=randint(0, int((end - start).total_seconds())))
    return str(date)[:10]


def generate_data(n):
    open("data.json", "w").close()
    fp = open("data.json", "w")
    productData = []
    for i in range(n):
        brand = randint(0, len(brands) - 1)
        subBrand = randint(0, len(subBrands[brand]) - 1)
        version = randint(versionRange[0], versionRange[1])
        rating = round(uniform(ratingRange[0], ratingRange[1]), 1)
        price = basePrices[brand][subBrand] * version * 0.5
        productData.append(
            template.format(
                brand=brands[brand],
                subBrand=subBrands[brand][subBrand],
                version=version,
                description=description(brand, subBrand, version),
                price=price,
                category=categories[brand][subBrand],
                image=images[brand][subBrand],
                date=date_generator(start, end),
                rating=rating,
            )
        )
    result = ",".join(productData)
    fp.write("[" + result + "]")

    # template data


template = '{{"name": "{brand} {subBrand}{version}","description": "{description}","brand": "{brand}","price": {price},"category": "{category}","image": "{image}","addedDate": "{date}","rating": {rating}}}'

descriptionTemplate = "Introducing our cutting-edge {brand} {subBrand}{version}, designed to revolutionize your life. This sleek and innovative {category} seamlessly combines form and function to enhance your everyday experiences. Whether you're a tech enthusiast, a busy professional, or simply someone looking to make life easier, this {category} is the perfect addition to your arsenal of gadgets. With its state-of-the-art features, this {category} empowers you to stay connected, productive, and entertained like never before. Its powerful performance ensures smooth multitasking, while its intuitive controls make it accessible to users of all skill levels. Experience unparalleled convenience and efficiency as you effortlessly navigate through tasks, whether it's for work, entertainment, or personal use. Its sleek design not only complements your modern lifestyle but also makes a bold statement about your commitment to quality and innovation. Trust in the reliability and durability of this {category}, crafted with precision and attention to detail. Every aspect has been carefully designed to exceed your expectations. Enhance your life today with this versatile {category}, available now on Circuit Cart. Join the ranks of satisfied customers who have already embraced the future of technology. Elevate your everyday and seize the possibilities that await with this exceptional {brand} {subBrand}{version} at your fingertips."


# products data

brands = ["Samsung", "Apple", "HP", "Google"]
subBrands = [
    ["Galaxy S2", "Galaxy Book "],
    ["iPhone ", "Macbook "],
    ["Omen 1", "Wireless Mouse "],
    ["Pixel ", "Pixel Buds "],
]
categories = [
    ["SmartPhone", "Laptop"],
    ["SmartPhone", "Laptop"],
    ["Laptop", "Accessory"],
    ["SmartPhone", "Accessory"],
]
basePrices = [[50000, 60000], [40000, 80000], [75000, 500], [35000, 1000]]
images = [
    [
        "https://rukminim2.flixcart.com/image/416/416/xif0q/mobile/q/q/w/galaxy-s23-ultra-5g-smartphone-sm-s918bzkcins-samsung-original-imagqjczezmgquhb.jpeg?q=70",
        "https://rukminim2.flixcart.com/image/416/416/l0r1j0w0/computer/z/m/a/np340xla-ka1in-thin-and-light-laptop-samsung-original-imagcgqvcvcbsun6.jpeg?q=70",
    ],
    [
        "https://rukminim2.flixcart.com/image/416/416/k2jbyq80pkrrdj/mobile-refurbished/k/y/d/iphone-11-256-u-mwm82hn-a-apple-0-original-imafkg25mhaztxns.jpeg?q=70",
        "https://rukminim2.flixcart.com/image/416/416/kp5sya80/screen-guard/tempered-glass/o/v/n/apple-macbook-air-m1-13-3-inch-lightwings-original-imag3gh5xftgbpg3.jpeg?q=70",
    ],
    [
        "https://rukminim2.flixcart.com/image/416/416/xif0q/computer/i/q/r/victus-15-fa-gaming-laptop-hp-original-imagpyfc64s6wwpb.jpeg?q=70",
        "https://rukminim2.flixcart.com/image/416/416/k0e66q80/mouse/u/8/6/hp-s1000-original-imafk74z7xnkmqyx.jpeg?q=70",
    ],
    [
        "https://rukminim2.flixcart.com/image/416/416/xif0q/mobile/z/b/d/-original-imagpgx48f4szdvf.jpeg?q=70",
        "https://rukminim2.flixcart.com/image/416/416/l5ld8y80/headphone/e/8/o/ga03201-google-original-imagg8d7bhxjduze.jpeg?q=70",
    ],
]
versionRange = [2, 5]
ratingRange = [3, 5]
start = datetime(2021, 1, 1)
end = datetime(2023, 9, 1)

count = 10
generate_data(count)
