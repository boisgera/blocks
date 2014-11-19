
"""
Coarse-grained Python Parser.

  - Meant to be used to parse high-level structure info and documentation
    (class, fcts, variables, docstring, comments).

  - Convention for documentation: "blocks" are separated with blanklines.
    Docstring may be used even if noone can see them, and should be parsed.
    Example: the code snippet

        a = 42
        "The answer"

    should document the global/local/attribute a.

  - Should work with Python and Cython.

  - See what's done in docgen, but reimplement with Plex ?
    (less hacks, cleaner ?) Evaluate the state of docgen first.

  - The key point is to fetch the indentation (block) structure, which
    means also the ability to understand indents/dedents, blanklines
    and implicit or explicit line continuation.

  - We DO NOT target automatic documentation anymore: the user will specify
    the 'stuff' he wants to be documented using a uniform doted syntax
    (that shall work for everything, including closures), and the source
    of info will be a mix of introspection (to support) dynamic tricks
    and static source analysis (for attributes, closures, etc.)

  - Think LONG AND HARD at the high-level (structure) document model:

        - uniform (or typed?) tree structure. Probably typed, but focus
          on iteration / attribute access first (type shall be obtained
          from a finer-grain analysis). 

        - nodes are hybrid list/attribute stuff, or let's say iterable
          with a dict of attributes ? (as in etree) ? Think of it.
          etree uses untyped stuff but with a tag id AND packs all
          attributes in a dict. The alternative is typed python objects
          that support iteration, and maybe a field that lists the attributes
          for generic algorithms.

        - all nodes contain source file info + line number ... + source ?
          With some invariants that we shall be able to regenerate ?
          (to support transformations ? Nah, we are read-only so far).

        - all the characters should belong to some node, so that it we
          concatenate the text content of all elements, we get the 
          source back.

        - support several iterators: iterblocks, iterlines, etc.
          SOMEHOW, that can be used to hide or transform the "true" structure
          of the AST that we use.
          Ex: iterlines return line objects that support unicode but also
          have a parent(s) field ?

        - what to do with line continuations (implicit or explicit) ?
          have a "LINECONT" token ? 

"""
