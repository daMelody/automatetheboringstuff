def spam():
    #! ERROR: print(eggs)
    #? what is causing this error
    eggs = 'spam local'
    print(eggs)


eggs = 'global'  # TODO: move this assignment above the function and uncomment the ERROR line
spam()
