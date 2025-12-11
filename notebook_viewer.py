"""
Olympic Medal Prediction - Notebook Viewer
A simple HTML viewer to display the Jupyter notebook content in a browser
similar to GitHub's notebook rendering.
"""

from IPython.display import HTML, display
import nbformat
from nbconvert import HTMLExporter
import argparse
import os
from pathlib import Path


def convert_notebook_to_html(notebook_path, output_path=None):
    """
    Convert a Jupyter notebook to HTML format.
    
    Args:
        notebook_path: Path to the . ipynb file
        output_path: Optional path for the output HTML file
    
    Returns:
        HTML content as string
    """
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Create HTML exporter with custom configuration
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'classic'
    
    # Convert notebook to HTML
    (body, resources) = html_exporter.from_notebook_node(notebook)
    
    # Add custom CSS for better styling
    custom_css = """
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding:  20px;
            background-color: #ffffff;
        }
        
        .notebook-header {
            background:  linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius:  10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .notebook-header h1 {
            margin: 0;
            font-size: 2.5em;
            font-weight: bold;
        }
        
        .notebook-header p {
            margin: 10px 0 0 0;
            font-size:  1.1em;
            opacity: 0.9;
        }
        
        .section-header {
            background-color: #f6f8fa;
            border-left: 4px solid #667eea;
            padding:  15px 20px;
            margin: 30px 0 15px 0;
            border-radius: 5px;
            font-size: 1.5em;
            font-weight: bold;
        }
        
        .cell {
            margin-bottom: 20px;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            overflow: hidden;
        }
        
        .input_area {
            background-color: #f6f8fa;
            padding: 15px;
            border-left: 3px solid #0366d6;
        }
        
        .output_area {
            background-color: #ffffff;
            padding: 15px;
            border-top: 1px solid #e1e4e8;
        }
        
        .prompt {
            color: #0366d6;
            font-weight: bold;
            margin-right: 10px;
        }
        
        .dataframe {
            border-collapse: collapse;
            margin: 10px 0;
            font-size: 0.9em;
            box-shadow: 0 2px 3px rgba(0,0,0,0.1);
        }
        
        . dataframe th {
            background-color: #667eea;
            color: white;
            padding: 12px;
            text-align:  left;
        }
        
        .dataframe td {
            padding: 10px;
            border-bottom:  1px solid #e1e4e8;
        }
        
        .dataframe tr:hover {
            background-color:  #f6f8fa;
        }
        
        pre {
            background-color: #f6f8fa;
            padding: 15px;
            border-radius:  5px;
            overflow-x: auto;
        }
        
        code {
            background-color: #f6f8fa;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 15px auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 5px;
        }
        
        . back-to-top {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #667eea;
            color: white;
            padding: 10px 15px;
            border-radius:  50px;
            text-decoration: none;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            transition: all 0.3 seconds;
        }
        
        .back-to-top:hover {
            background-color: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
    </style>
    """
    
    # Create complete HTML document
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Olympic Medal Prediction - Athletes Analysis</title>
        {custom_css}
    </head>
    <body>
        <div class="notebook-header">
            <h1>🏅 Olympic Medal Prediction</h1>
            <p>Interactive analysis and machine learning model for predicting Olympic medals</p>
        </div>
        
        <div class="section-header">📊 Hypothesis</div>
        <p>We can predict how many medals a country will win at the Olympics by using historical data.</p>
        
        <div class="section-header">📁 The Data</div>
        <p>A dataset of how many medals each country won at each Olympics.  Additional data includes number of athletes, average age, and previous medal counts.</p>
        
        {body}
        
        <a href="#top" class="back-to-top">↑ Top</a>
        
        <script>
            // Add smooth scrolling
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        </script>
    </body>
    </html>
    """
    
    # Save to file if output path is provided
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ HTML file created:  {output_path}")
    
    return html_content


def serve_notebook(html_path, port=8000):
    """
    Serve the HTML file using Python's built-in HTTP server.
    
    Args:
        html_path: Path to the HTML file
        port: Port number to serve on (default: 8000)
    """
    import http.server
    import socketserver
    import os
    
    # Change to the directory containing the HTML file
    os.chdir(os.path.dirname(os.path.abspath(html_path)))
    filename = os.path.basename(html_path)
    
    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory='.', **kwargs)
        
        def end_headers(self):
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            super().end_headers()
    
    with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
        print(f"🌐 Serving notebook at http://localhost:{port}/{filename}")
        print("📌 Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n⛔ Server stopped")


def main():
    """
    Main function to run the notebook viewer from command line.
    """
    parser = argparse.ArgumentParser(
        description="Convert and view Jupyter notebooks as HTML"
    )
    parser.add_argument(
        "notebook",
        nargs='?',
        default="Athletes.ipynb",
        help="Path to the Jupyter notebook file (default: Athletes.ipynb)"
    )
    parser.add_argument(
        "-o", "--output",
        default="notebook_view.html",
        help="Output HTML file path (default: notebook_view.html)"
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        default=8000,
        help="Port number to serve on (default: 8000)"
    )
    parser.add_argument(
        "--no-serve",
        action="store_true",
        help="Don't start the web server after conversion"
    )
    
    args = parser.parse_args()
    
    # Check if notebook file exists
    if not os. path.exists(args.notebook):
        print(f"❌ Error: Notebook file '{args.notebook}' not found!")
        return
    
    # Convert notebook to HTML
    print(f"🔄 Converting {args.notebook} to HTML...")
    convert_notebook_to_html(args.notebook, args.output)
    
    # Serve the HTML file
    if not args.no_serve:
        print("\n" + "="*50)
        serve_notebook(args.output, args.port)


if __name__ == "__main__":
    # If running directly, convert the default notebook
    if not any(arg in __import__('sys').argv for arg in ['-h', '--help']):
        main()
    else:
        main()
