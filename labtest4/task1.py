import json
import shutil
import subprocess

# task1.py
# Demonstrate a Python list comprehension that filters even numbers,
# show equivalent JavaScript code, run it with Node (if available),
# and print a short comparison of syntax and output.


numbers = list(range(10))
evens_py = [x for x in numbers if x % 2 == 0]

js_code = """
const numbers = [0,1,2,3,4,5,6,7,8,9];
const evens = numbers.filter(x => x % 2 === 0);
console.log(JSON.stringify(evens));
""".strip()

# Try to run the JS snippet with Node if installed
node_path = shutil.which("node")
js_output = None
node_err = None
if node_path:
    try:
        proc = subprocess.run([node_path, "-e", js_code],
                              capture_output=True, text=True, check=False)
        js_output = proc.stdout.strip()
        node_err = proc.stderr.strip() or None
    except Exception as e:
        node_err = str(e)
else:
    node_err = "node not found on PATH"

# Print results
print("Python list comprehension result:", evens_py)
print("\nEquivalent JavaScript code:\n" + js_code)
if js_output is not None:
    try:
        evens_js_parsed = json.loads(js_output)
    except Exception:
        evens_js_parsed = js_output
    print("\nJavaScript output (raw):", js_output)
    print("JavaScript output parsed:", evens_js_parsed)
else:
    print("\nJavaScript execution skipped:", node_err)

# Short comparison
print("\nComparison:")
print("- Syntax: Python: [x for x in sequence if condition]")
print("          JavaScript: sequence.filter(x => condition)")
print("- Equality/operator note: JS uses === for strict equality; here % works the same.")
print("- Output formatting: Python prints a Python list repr (e.g. [0, 2, 4, ...]);")
print("                    JS console.log(JSON.stringify(...)) prints JSON (e.g. [0,2,4,...])")
print("- Types/values: Both produce arrays/lists of integers with the same values.")