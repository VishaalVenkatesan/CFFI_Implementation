import os
from cffi import FFI

# Define the file path
current_directory = os.path.dirname(os.path.abspath(__file__))
c_file_path = os.path.join(current_directory, 'AVL.c')

# Reading the C source file
with open(c_file_path, 'r') as c_file:
    c_source_code = c_file.read()

# Create FFI builder
ffi_builder = FFI()

# Define the C header (contains only function prototypes and type definitions)
header = '''
    struct Node {
        struct Node *LeftChild;
        int data;
        int bf;
        struct Node *RightChild;
    };

    typedef struct Node Node;

    Node *RInsert(Node *p, int key);
    void Inorder(Node *p);
    Node *Search(int key);
    int height(Node *p);
    Node *LLRotation(Node *p);
    Node *LRRotation(Node *p);
    Node *RRRotation(Node *p);
    Node *RLRotation(Node *p);
'''

# Attach the header to the FFI builder
ffi_builder.cdef(header)

# Set up the module name and source code
module_name = 'AVL_Module'
ffi_builder.set_source(module_name, c_source_code)

# Compile the CFFI extension module
if __name__ == '__main__':
    ffi_builder.compile()




