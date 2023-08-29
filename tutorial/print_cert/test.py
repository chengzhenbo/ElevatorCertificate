from generate_pdf import generate_report,generate_reports

def test_one_pdf():
    
    report_data = {
        "title": "Ad9u9231",
        "description": "This is a summary of the product sales.",
        "products": [
            {"name": "Product A", "quantity": 100, "price": 15},
            {"name": "Product B", "quantity": 50, "price": 20},
            {"name": "Product C", "quantity": 75, "price": 12},
        ],
    }
    pdf_file = generate_report(report_data)
    print(pdf_file)

def test_many_pdf():
    
    report_data1 = '{"title": "ERasdf394", "age": 30}'
    report_data2 = '{"title": "DDAlice23", "age": 30}'

    pdf_file = generate_reports(report_data1,report_data2)
    print(pdf_file)
if __name__ == "__main__":
    test_one_pdf()