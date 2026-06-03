! subroutines are like functions that don't have a return value

subroutine add_one(a)

    ! in means the caller provides a value (like a parameter)
    ! out means the subroutine can modify it
    ! inout means both
    integer, intent (inout) :: a
    a = a + 1

end subroutine


program myApp

    integer :: x

    x = 5

    call add_one(x)

    print *, x


end program myApp