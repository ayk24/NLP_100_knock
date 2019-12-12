from string import Template


def gen_template(x, y, z):
    template = Template("$hour時の$temperatureは$value")
    return template.substitute(hour=x, temperature=y, value=z)


print(gen_template("12", "気温", "22.4"))
