! Copied from https://github.com/ROCmSoftwarePlatform/hipfort/tree/develop/test/f2008/vecadd
program fortran_hip
  use hipfort
  use hipfort_check
  
  implicit none

  interface
     ! dim3(320), dim3(256), 0, 0
     subroutine launch(grid,block,shmem,stream,out,a,b,N) bind(c)
       use iso_c_binding
       use hipfort_types
       implicit none
       type(c_ptr),value :: a, b, out
       integer(c_int), value :: N, shmem
       type(dim3) :: grid, block
       type(c_ptr),value :: stream
     end subroutine
  end interface

  integer(c_int), parameter :: N = 1000000

  real(8),allocatable,dimension(:) :: a,b,out
  real(8),pointer,dimension(:) :: da => null(), db => null(),dout => null()

  !type(dim3) :: grid  = dim3(320,1,1) 
  !type(dim3) :: block = dim3(256,1,1) 
  
  integer :: i
  type(hipDeviceProp_t),target :: props
  !
  call hipCheck(hipGetDeviceProperties(props,0))  
  write(*,"(a)",advance="no") "-- Running test 'vecadd' (Fortran 2008 interfaces)"
  write(*,"(a)",advance="no") "- device: "
  i=1
  do while ( iachar(props%name(i)) .ne. 0 ) ! print till end char
    write(*,"(a)",advance="no") props%name(i)
    i = i+1
  end do 
  write(*,"(a)",advance="no") " - "

  ! Allocate host memory
  allocate(a(N),b(N),out(N))

  ! Initialize host arrays
  a(:) = 1.0
  b(:) = 1.0

  ! Allocate array space on the device
  call hipCheck(hipMalloc(da,N))
  call hipCheck(hipMalloc(db,N))
  call hipCheck(hipMalloc(dout,N))

  ! Transfer data from host to device memory
  call hipCheck(hipMemcpy(da, a, N, hipMemcpyHostToDevice))
  call hipCheck(hipMemcpy(db, b, N, hipMemcpyHostToDevice))

  ! launch kernel
  call launch(dim3(320),dim3(256),0,c_null_ptr,c_loc(dout),c_loc(da),c_loc(db),N)
  !call launch(grid,block,0,c_null_ptr,c_loc(dout),c_loc(da),c_loc(db),N)
  call hipCheck(hipDeviceSynchronize())

  ! Transfer data back to host memory
  call hipCheck(hipMemcpy(out, dout, N, hipMemcpyDeviceToHost))

  if ( sum(out) .eq. N*2.0 ) then
     print *, "PASSED!"
  else
     print *, "FAILED!"
  endif

  call hipCheck(hipFree(da))
  call hipCheck(hipFree(db))
  call hipCheck(hipFree(dout))

  ! Deallocate host memory
  deallocate(a,b,out)

end program fortran_hip
