/^CPPFLAGS/s/$/ -DWE_ARE_PROFILING/
/^CFLAGS/s/$/ -glldb -O0/
/^LDFLAGS/s/$/ -Wl,no_pie/
