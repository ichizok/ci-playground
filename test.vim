set rtp^=/tmp/vim-perf
call vimperf#setup()
function Estimate(n, t)
  call vimperf#start('prof_'..a:t..'.out')
  let start = reltime()
  for _ in range(a:n)
    execute 'sleep' a:t
  endfor
  let elapsed = reltimefloat(reltime(start))
  call vimperf#stop()
  let calibrator = (a:n * a:t * (a:t =~# 'm$' ? 1 : 1000)) / (elapsed * 1000)
  echo printf('%dx sleep %s', a:n, a:t)
  echo printf('Elapsed     = %f', elapsed)
  echo printf('Calibration = %f', calibrator)
  echo ''
endfunction
function VMMap(fname)
  call writefile(systemlist('vmmap '..getpid()), a:fname)
endfunction
" sleep 1
" call Estimate(1000, '1m')
" call Estimate(100, '10m')
" call Estimate(10, '100m')
" call Estimate(1, '1000m')
