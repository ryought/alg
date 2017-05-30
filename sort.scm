(define (string>=? x y) (or (string>? x y) (string=? x y)))




;;;;;;;;;;;;;;;;;;;;
;;;;; quick sort
;;;;;;;;;;;;;;;;;;;;
;; 参考文献
;; http://chamaken.blogspot.jp/2009/12/lisp-quicksort.html
;; https://en.wikipedia.org/wiki/Quicksort
(define (qsort l)
  (if (null? l)
      '()
      (let* ((x (car l))
             (r (cdr l)))
        (append  (qsort (filter (lambda (a) (string<? a x)) r))
                 (list x)
                 (qsort (filter (lambda (a) (string>=? a x)) r))))))




