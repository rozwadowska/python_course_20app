contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "This slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(contents, filenames):
    file = open(f"files/{filenames}", "w")
    file.write(content)