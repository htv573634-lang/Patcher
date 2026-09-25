import os
import re
import sys
import glob

def analyze_compilation_errors(log_file):
    """Analyze compilation errors and identify Python 3.13 incompatibilities"""
    if not os.path.exists(log_file):
        return []
        
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    patterns = {
        'Py_TYPE_assignment': r"error: assignment to read-only location.*Py_TYPE",
        'PyEval_CallObject': r"error: implicit declaration of function 'PyEval_CallObject'",
        'PyObject_Call': r"error: implicit declaration of function 'PyObject_Call'",
    }
    
    issues = []
    for issue_name, pattern in patterns.items():
        if re.search(pattern, log_content):
            issues.append(issue_name)
    
    return issues

def generate_patch(content, issues):
    """Apply fixes for common Python 3.13 issues"""
    patched_content = content
    
    if 'Py_TYPE_assignment' in issues:
        patched_content = re.sub(
            r'Py_TYPE\((\w+)\)\s*=\s*([^;]+);',
            r'Py_SET_TYPE(\1, \2);',
            patched_content
        )
    
    if 'PyEval_CallObject' in issues:
        patched_content = re.sub(
            r'PyEval_CallObject\(([^,]+),\s*([^)]+)\)',
            r'PyObject_Call(\1, \2, NULL)',
            patched_content
        )
        
    return patched_content

def main():
    log_file = '../build-logs/initial-build.log'
    issues = analyze_compilation_errors(log_file)
    
    if not issues:
        print("No known Python 3.13 C-API issues detected in build log.")
        return
    
    print(f"Detected issues to patch: {issues}")
    
    cpp_files = glob.glob('**/*.cpp', recursive=True) + \
                glob.glob('**/*.cu', recursive=True) + \
                glob.glob('**/*.h', recursive=True)
                
    patched_count = 0
    
    for cpp_file in cpp_files:
        try:
            with open(cpp_file, 'r') as f:
                original = f.read()
            
            patched = generate_patch(original, issues)
            
            if patched != original:
                with open(cpp_file, 'w') as f:
                    f.write(patched)
                patched_count += 1
                print(f"Patched: {cpp_file}")
        except Exception as e:
            print(f"Error processing {cpp_file}: {e}")
    
    print(f"\nPatch complete. {patched_count} files modified.")

if __name__ == "__main__":
    main()
