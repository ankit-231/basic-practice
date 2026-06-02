! this is a comment
! Source: [FORTRAN in 100 Seconds - YouTube](https://www.youtube.com/watch?v=NMWzgy8FsKs)
! Used https://www.onlinegdb.com/online_fortran_compiler for compiler

program myApp

    implicit none
    
    integer :: age = 99
    
    ! if you don't set the correct length, only the specified length will be printed. Eg: for len=5, only Hello would be printed
    character(len = 12) :: greeting
    
    real, dimension(5) :: list = 0.0
    
    ! same way of writing above
    real, dimension(5) :: lista = [0.0, 0.0, 0.0, 0.0, 0.0]
    
    
    
    ! all declarations must be before any executable statements, even assignments
    
    
    real, allocatable :: ptr
    
    allocate (ptr)
    
    ptr = 3.14
    
    print *, ptr
    
    deallocate (ptr)
    
    ! below is an executable statement
    greeting = "Hello World!"
    
    print *, greeting
    
    print *, list
    
    print *, lista

end program myApp