integer function ten_times(val) result(res)
    ! input
    integer, intent(in) :: val

    ! return value
    res = val * 10

end function ten_times

program myApp
    implicit none

    integer :: ten_times

    print *, ten_times(5)

end program myApp