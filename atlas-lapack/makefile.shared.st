include Make.inc

all: libatlas.so libf77blas.so libcblas.so libblas.so liblapack.so.3.6.1

libatlas.so: libatlas.a
	ld $(LDFLAGS) -shared -soname $@ -o $@ --whole-archive libatlas.a \
	   --no-whole-archive -lc $(LIBS)

libf77blas.so : libf77blas.a libatlas.so
	ld $(LDFLAGS) -shared -soname libblas.so.3 -o $@ --whole-archive \
	   libf77blas.a --no-whole-archive $(F77SYSLIB) -L. -latlas

libcblas.so : libcblas.a libatlas.so libblas.so
	ld $(LDFLAGS) -shared -soname $@ -o $@ --whole-archive libcblas.a \
	    -L. -latlas -lblas

libblas.so: libf77blas.so
	ln -s $< $@

liblapack.so.3.6.1 : liblapack.a libcblas.so libblas.so
	ld $(LDFLAGS) -shared -soname liblapack.so.3 -o $@ --whole-archive \
	   liblapack.a --no-whole-archive $(F77SYSLIB) -L. -lcblas -lblas

liblapack.so.3: liblapack.so.3.6.1
	ln -s $< $@
