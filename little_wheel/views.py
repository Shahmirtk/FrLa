from django.shortcuts import render

# Create your views here.
def color_finder(number_li):
	color_li = []
	red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
	black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]

	for nu in number_li:
		if nu in red:
			color_li.append([nu, "red"])
		elif nu in black:
			color_li.append([nu, "black"])
		else:
			color_li.append([nu, "green"])
	return color_li

def index(request):
	number_li = [19, 4, 25, 6, 0, 23, 30, 16]
	color_li = color_finder(number_li)
	latest = color_li[-1]
	return render(request, "little_wheel/index.html", {
		"color_li": color_li[:-1], "latest": latest
		})