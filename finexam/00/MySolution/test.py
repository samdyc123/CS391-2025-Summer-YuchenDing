import sys
sys.setrecursionlimit(10000000)

def fun123(args):
    # Generated Python code from LAMBDA compilation
    tmp486 = args[0]
    tmp487 = args[1]
    tmp488 = tmp487[0]
    tmp489 = args[1]
    tmp490 = tmp489[1]
    tmp491 = tmp490[0]
    tmp492 = args[1]
    tmp493 = tmp492[1]
    tmp494 = tmp493[1]
    tmp495 = 8
    tmp496 = tmp491 < tmp495
    if tmp496:
        # Generated Python code from LAMBDA compilation
        def fun124(args):
            # Generated Python code from LAMBDA compilation
            tmp497 = args[0]
            tmp498 = args[1]
            tmp499 = tmp498[0]
            tmp500 = args[1]
            tmp501 = tmp500[1]
            tmp502 = tmp501[0]
            tmp503 = args[1]
            tmp504 = tmp503[1]
            tmp505 = tmp504[1]
            tmp506 = 0
            tmp507 = tmp505 >= tmp506
            if tmp507:
                # Generated Python code from LAMBDA compilation
                def fun125(i0):
                    # Generated Python code from LAMBDA compilation
                    def fun126(j0):
                        # Generated Python code from LAMBDA compilation
                        def fun127(i):
                            # Generated Python code from LAMBDA compilation
                            def fun128(j):
                                # Generated Python code from LAMBDA compilation
                                tmp508 = j0 != j
                                tmp509 = i0 - i
                                tmp510 = abs(tmp509)
                                tmp511 = j0 - j
                                tmp512 = abs(tmp511)
                                tmp513 = tmp510 != tmp512
                                tmp514 = tmp508 and tmp513
                                # Result is in tmp514
                                return tmp514
                            # Result is in fun128
                            return fun128
                        # Result is in fun127
                        return fun127
                    # Result is in fun126
                    return fun126
                tmp515 = fun125(tmp497)
                tmp516 = tmp515(tmp499)
                tmp517 = tmp516(tmp505)
                def fun129(board):
                    # Generated Python code from LAMBDA compilation
                    def fun130(i):
                        # Generated Python code from LAMBDA compilation
                        tmp518 = 0
                        tmp519 = i == tmp518
                        if tmp519:
                            # Generated Python code from LAMBDA compilation
                            tmp520 = board[0]
                            # Result is in tmp520
                            return tmp520
                        else:
                            # Generated Python code from LAMBDA compilation
                            tmp521 = 1
                            tmp522 = i == tmp521
                            if tmp522:
                                # Generated Python code from LAMBDA compilation
                                tmp523 = board[1]
                                tmp524 = tmp523[0]
                                # Result is in tmp524
                                return tmp524
                            else:
                                # Generated Python code from LAMBDA compilation
                                tmp525 = 2
                                tmp526 = i == tmp525
                                if tmp526:
                                    # Generated Python code from LAMBDA compilation
                                    tmp527 = board[1]
                                    tmp528 = tmp527[1]
                                    tmp529 = tmp528[0]
                                    # Result is in tmp529
                                    return tmp529
                                else:
                                    # Generated Python code from LAMBDA compilation
                                    tmp530 = 3
                                    tmp531 = i == tmp530
                                    if tmp531:
                                        # Generated Python code from LAMBDA compilation
                                        tmp532 = board[1]
                                        tmp533 = tmp532[1]
                                        tmp534 = tmp533[1]
                                        tmp535 = tmp534[0]
                                        # Result is in tmp535
                                        return tmp535
                                    else:
                                        # Generated Python code from LAMBDA compilation
                                        tmp536 = 4
                                        tmp537 = i == tmp536
                                        if tmp537:
                                            # Generated Python code from LAMBDA compilation
                                            tmp538 = board[1]
                                            tmp539 = tmp538[1]
                                            tmp540 = tmp539[1]
                                            tmp541 = tmp540[1]
                                            tmp542 = tmp541[0]
                                            # Result is in tmp542
                                            return tmp542
                                        else:
                                            # Generated Python code from LAMBDA compilation
                                            tmp543 = 5
                                            tmp544 = i == tmp543
                                            if tmp544:
                                                # Generated Python code from LAMBDA compilation
                                                tmp545 = board[1]
                                                tmp546 = tmp545[1]
                                                tmp547 = tmp546[1]
                                                tmp548 = tmp547[1]
                                                tmp549 = tmp548[1]
                                                tmp550 = tmp549[0]
                                                # Result is in tmp550
                                                return tmp550
                                            else:
                                                # Generated Python code from LAMBDA compilation
                                                tmp551 = 6
                                                tmp552 = i == tmp551
                                                if tmp552:
                                                    # Generated Python code from LAMBDA compilation
                                                    tmp553 = board[1]
                                                    tmp554 = tmp553[1]
                                                    tmp555 = tmp554[1]
                                                    tmp556 = tmp555[1]
                                                    tmp557 = tmp556[1]
                                                    tmp558 = tmp557[1]
                                                    tmp559 = tmp558[0]
                                                    # Result is in tmp559
                                                    return tmp559
                                                else:
                                                    # Generated Python code from LAMBDA compilation
                                                    tmp560 = 7
                                                    tmp561 = i == tmp560
                                                    if tmp561:
                                                        # Generated Python code from LAMBDA compilation
                                                        tmp562 = board[1]
                                                        tmp563 = tmp562[1]
                                                        tmp564 = tmp563[1]
                                                        tmp565 = tmp564[1]
                                                        tmp566 = tmp565[1]
                                                        tmp567 = tmp566[1]
                                                        tmp568 = tmp567[1]
                                                        # Result is in tmp568
                                                        return tmp568
                                                    else:
                                                        # Generated Python code from LAMBDA compilation
                                                        tmp569 = -1
                                                        # Result is in tmp569
                                                        return tmp569
                                                    tmp570 = tmp568
                                                    # Result is in tmp570
                                                    return tmp570
                                                tmp571 = tmp559
                                                # Result is in tmp571
                                                return tmp571
                                            tmp572 = tmp550
                                            # Result is in tmp572
                                            return tmp572
                                        tmp573 = tmp542
                                        # Result is in tmp573
                                        return tmp573
                                    tmp574 = tmp535
                                    # Result is in tmp574
                                    return tmp574
                                tmp575 = tmp529
                                # Result is in tmp575
                                return tmp575
                            tmp576 = tmp524
                            # Result is in tmp576
                            return tmp576
                        tmp577 = tmp520
                        # Result is in tmp577
                        return tmp577
                    # Result is in fun130
                    return fun130
                tmp578 = fun129(tmp502)
                tmp579 = tmp578(tmp505)
                tmp580 = tmp517(tmp579)
                if tmp580:
                    # Generated Python code from LAMBDA compilation
                    tmp581 = 1
                    tmp582 = tmp505 - tmp581
                    tmp583 = (tmp502, tmp582)
                    tmp584 = (tmp499, tmp583)
                    tmp585 = (tmp497, tmp584)
                    tmp586 = fun124(tmp585)
                    # Result is in tmp586
                    return tmp586
                else:
                    # Generated Python code from LAMBDA compilation
                    tmp587 = False
                    # Result is in tmp587
                    return tmp587
                tmp588 = tmp586
                # Result is in tmp588
                return tmp588
            else:
                # Generated Python code from LAMBDA compilation
                tmp589 = True
                # Result is in tmp589
                return tmp589
            tmp590 = tmp588
            # Result is in tmp590
            return tmp590
        tmp591 = 1
        tmp592 = tmp488 - tmp591
        tmp593 = (tmp486, tmp592)
        tmp594 = (tmp491, tmp593)
        tmp595 = (tmp488, tmp594)
        tmp596 = fun124(tmp595)
        if tmp596:
            # Generated Python code from LAMBDA compilation
            def fun131(board):
                # Generated Python code from LAMBDA compilation
                def fun132(i):
                    # Generated Python code from LAMBDA compilation
                    def fun133(j):
                        # Generated Python code from LAMBDA compilation
                        tmp597 = board[0]
                        tmp598 = board[1]
                        tmp599 = tmp598[0]
                        tmp600 = board[1]
                        tmp601 = tmp600[1]
                        tmp602 = tmp601[0]
                        tmp603 = board[1]
                        tmp604 = tmp603[1]
                        tmp605 = tmp604[1]
                        tmp606 = tmp605[0]
                        tmp607 = board[1]
                        tmp608 = tmp607[1]
                        tmp609 = tmp608[1]
                        tmp610 = tmp609[1]
                        tmp611 = tmp610[0]
                        tmp612 = board[1]
                        tmp613 = tmp612[1]
                        tmp614 = tmp613[1]
                        tmp615 = tmp614[1]
                        tmp616 = tmp615[1]
                        tmp617 = tmp616[0]
                        tmp618 = board[1]
                        tmp619 = tmp618[1]
                        tmp620 = tmp619[1]
                        tmp621 = tmp620[1]
                        tmp622 = tmp621[1]
                        tmp623 = tmp622[1]
                        tmp624 = tmp623[0]
                        tmp625 = board[1]
                        tmp626 = tmp625[1]
                        tmp627 = tmp626[1]
                        tmp628 = tmp627[1]
                        tmp629 = tmp628[1]
                        tmp630 = tmp629[1]
                        tmp631 = tmp630[1]
                        tmp632 = 0
                        tmp633 = i == tmp632
                        if tmp633:
                            # Generated Python code from LAMBDA compilation
                            tmp634 = (tmp624, tmp631)
                            tmp635 = (tmp617, tmp634)
                            tmp636 = (tmp611, tmp635)
                            tmp637 = (tmp606, tmp636)
                            tmp638 = (tmp602, tmp637)
                            tmp639 = (tmp599, tmp638)
                            tmp640 = (j, tmp639)
                            # Result is in tmp640
                            return tmp640
                        else:
                            # Generated Python code from LAMBDA compilation
                            tmp641 = 1
                            tmp642 = i == tmp641
                            if tmp642:
                                # Generated Python code from LAMBDA compilation
                                tmp643 = (tmp624, tmp631)
                                tmp644 = (tmp617, tmp643)
                                tmp645 = (tmp611, tmp644)
                                tmp646 = (tmp606, tmp645)
                                tmp647 = (tmp602, tmp646)
                                tmp648 = (j, tmp647)
                                tmp649 = (tmp597, tmp648)
                                # Result is in tmp649
                                return tmp649
                            else:
                                # Generated Python code from LAMBDA compilation
                                tmp650 = 2
                                tmp651 = i == tmp650
                                if tmp651:
                                    # Generated Python code from LAMBDA compilation
                                    tmp652 = (tmp624, tmp631)
                                    tmp653 = (tmp617, tmp652)
                                    tmp654 = (tmp611, tmp653)
                                    tmp655 = (tmp606, tmp654)
                                    tmp656 = (j, tmp655)
                                    tmp657 = (tmp599, tmp656)
                                    tmp658 = (tmp597, tmp657)
                                    # Result is in tmp658
                                    return tmp658
                                else:
                                    # Generated Python code from LAMBDA compilation
                                    tmp659 = 3
                                    tmp660 = i == tmp659
                                    if tmp660:
                                        # Generated Python code from LAMBDA compilation
                                        tmp661 = (tmp624, tmp631)
                                        tmp662 = (tmp617, tmp661)
                                        tmp663 = (tmp611, tmp662)
                                        tmp664 = (j, tmp663)
                                        tmp665 = (tmp602, tmp664)
                                        tmp666 = (tmp599, tmp665)
                                        tmp667 = (tmp597, tmp666)
                                        # Result is in tmp667
                                        return tmp667
                                    else:
                                        # Generated Python code from LAMBDA compilation
                                        tmp668 = 4
                                        tmp669 = i == tmp668
                                        if tmp669:
                                            # Generated Python code from LAMBDA compilation
                                            tmp670 = (tmp624, tmp631)
                                            tmp671 = (tmp617, tmp670)
                                            tmp672 = (j, tmp671)
                                            tmp673 = (tmp606, tmp672)
                                            tmp674 = (tmp602, tmp673)
                                            tmp675 = (tmp599, tmp674)
                                            tmp676 = (tmp597, tmp675)
                                            # Result is in tmp676
                                            return tmp676
                                        else:
                                            # Generated Python code from LAMBDA compilation
                                            tmp677 = 5
                                            tmp678 = i == tmp677
                                            if tmp678:
                                                # Generated Python code from LAMBDA compilation
                                                tmp679 = (tmp624, tmp631)
                                                tmp680 = (j, tmp679)
                                                tmp681 = (tmp611, tmp680)
                                                tmp682 = (tmp606, tmp681)
                                                tmp683 = (tmp602, tmp682)
                                                tmp684 = (tmp599, tmp683)
                                                tmp685 = (tmp597, tmp684)
                                                # Result is in tmp685
                                                return tmp685
                                            else:
                                                # Generated Python code from LAMBDA compilation
                                                tmp686 = 6
                                                tmp687 = i == tmp686
                                                if tmp687:
                                                    # Generated Python code from LAMBDA compilation
                                                    tmp688 = (j, tmp631)
                                                    tmp689 = (tmp617, tmp688)
                                                    tmp690 = (tmp611, tmp689)
                                                    tmp691 = (tmp606, tmp690)
                                                    tmp692 = (tmp602, tmp691)
                                                    tmp693 = (tmp599, tmp692)
                                                    tmp694 = (tmp597, tmp693)
                                                    # Result is in tmp694
                                                    return tmp694
                                                else:
                                                    # Generated Python code from LAMBDA compilation
                                                    tmp695 = 7
                                                    tmp696 = i == tmp695
                                                    if tmp696:
                                                        # Generated Python code from LAMBDA compilation
                                                        tmp697 = (tmp624, j)
                                                        tmp698 = (tmp617, tmp697)
                                                        tmp699 = (tmp611, tmp698)
                                                        tmp700 = (tmp606, tmp699)
                                                        tmp701 = (tmp602, tmp700)
                                                        tmp702 = (tmp599, tmp701)
                                                        tmp703 = (tmp597, tmp702)
                                                        # Result is in tmp703
                                                        return tmp703
                                                    else:
                                                        # Generated Python code from LAMBDA compilation
                                                        # Result is in board
                                                        return board
                                                    tmp704 = tmp703
                                                    # Result is in tmp704
                                                    return tmp704
                                                tmp705 = tmp694
                                                # Result is in tmp705
                                                return tmp705
                                            tmp706 = tmp685
                                            # Result is in tmp706
                                            return tmp706
                                        tmp707 = tmp676
                                        # Result is in tmp707
                                        return tmp707
                                    tmp708 = tmp667
                                    # Result is in tmp708
                                    return tmp708
                                tmp709 = tmp658
                                # Result is in tmp709
                                return tmp709
                            tmp710 = tmp649
                            # Result is in tmp710
                            return tmp710
                        tmp711 = tmp640
                        # Result is in tmp711
                        return tmp711
                    # Result is in fun133
                    return fun133
                # Result is in fun132
                return fun132
            tmp712 = fun131(tmp486)
            tmp713 = tmp712(tmp488)
            tmp714 = tmp713(tmp491)
            tmp715 = 1
            tmp716 = tmp488 + tmp715
            tmp717 = 8
            tmp718 = tmp716 == tmp717
            if tmp718:
                # Generated Python code from LAMBDA compilation
                tmp719 = (tmp486, tmp494)
                print(tmp719); tmp720 = 0
                tmp721 = 1
                tmp722 = tmp491 + tmp721
                tmp723 = 1
                tmp724 = tmp494 + tmp723
                tmp725 = (tmp722, tmp724)
                tmp726 = (tmp488, tmp725)
                tmp727 = (tmp486, tmp726)
                tmp728 = fun123(tmp727)
                # Result is in tmp728
                return tmp728
            else:
                # Generated Python code from LAMBDA compilation
                tmp729 = 1
                tmp730 = tmp488 + tmp729
                tmp731 = 0
                tmp732 = (tmp731, tmp494)
                tmp733 = (tmp730, tmp732)
                tmp734 = (tmp714, tmp733)
                tmp735 = fun123(tmp734)
                # Result is in tmp735
                return tmp735
            tmp736 = tmp728
            # Result is in tmp736
            return tmp736
        else:
            # Generated Python code from LAMBDA compilation
            tmp737 = 1
            tmp738 = tmp491 + tmp737
            tmp739 = (tmp738, tmp494)
            tmp740 = (tmp488, tmp739)
            tmp741 = (tmp486, tmp740)
            tmp742 = fun123(tmp741)
            # Result is in tmp742
            return tmp742
        tmp743 = tmp736
        # Result is in tmp743
        return tmp743
    else:
        # Generated Python code from LAMBDA compilation
        tmp744 = 0
        tmp745 = tmp488 > tmp744
        if tmp745:
            # Generated Python code from LAMBDA compilation
            tmp746 = 1
            tmp747 = tmp488 - tmp746
            def fun134(board):
                # Generated Python code from LAMBDA compilation
                def fun135(i):
                    # Generated Python code from LAMBDA compilation
                    tmp748 = 0
                    tmp749 = i == tmp748
                    if tmp749:
                        # Generated Python code from LAMBDA compilation
                        tmp750 = board[0]
                        # Result is in tmp750
                        return tmp750
                    else:
                        # Generated Python code from LAMBDA compilation
                        tmp751 = 1
                        tmp752 = i == tmp751
                        if tmp752:
                            # Generated Python code from LAMBDA compilation
                            tmp753 = board[1]
                            tmp754 = tmp753[0]
                            # Result is in tmp754
                            return tmp754
                        else:
                            # Generated Python code from LAMBDA compilation
                            tmp755 = 2
                            tmp756 = i == tmp755
                            if tmp756:
                                # Generated Python code from LAMBDA compilation
                                tmp757 = board[1]
                                tmp758 = tmp757[1]
                                tmp759 = tmp758[0]
                                # Result is in tmp759
                                return tmp759
                            else:
                                # Generated Python code from LAMBDA compilation
                                tmp760 = 3
                                tmp761 = i == tmp760
                                if tmp761:
                                    # Generated Python code from LAMBDA compilation
                                    tmp762 = board[1]
                                    tmp763 = tmp762[1]
                                    tmp764 = tmp763[1]
                                    tmp765 = tmp764[0]
                                    # Result is in tmp765
                                    return tmp765
                                else:
                                    # Generated Python code from LAMBDA compilation
                                    tmp766 = 4
                                    tmp767 = i == tmp766
                                    if tmp767:
                                        # Generated Python code from LAMBDA compilation
                                        tmp768 = board[1]
                                        tmp769 = tmp768[1]
                                        tmp770 = tmp769[1]
                                        tmp771 = tmp770[1]
                                        tmp772 = tmp771[0]
                                        # Result is in tmp772
                                        return tmp772
                                    else:
                                        # Generated Python code from LAMBDA compilation
                                        tmp773 = 5
                                        tmp774 = i == tmp773
                                        if tmp774:
                                            # Generated Python code from LAMBDA compilation
                                            tmp775 = board[1]
                                            tmp776 = tmp775[1]
                                            tmp777 = tmp776[1]
                                            tmp778 = tmp777[1]
                                            tmp779 = tmp778[1]
                                            tmp780 = tmp779[0]
                                            # Result is in tmp780
                                            return tmp780
                                        else:
                                            # Generated Python code from LAMBDA compilation
                                            tmp781 = 6
                                            tmp782 = i == tmp781
                                            if tmp782:
                                                # Generated Python code from LAMBDA compilation
                                                tmp783 = board[1]
                                                tmp784 = tmp783[1]
                                                tmp785 = tmp784[1]
                                                tmp786 = tmp785[1]
                                                tmp787 = tmp786[1]
                                                tmp788 = tmp787[1]
                                                tmp789 = tmp788[0]
                                                # Result is in tmp789
                                                return tmp789
                                            else:
                                                # Generated Python code from LAMBDA compilation
                                                tmp790 = 7
                                                tmp791 = i == tmp790
                                                if tmp791:
                                                    # Generated Python code from LAMBDA compilation
                                                    tmp792 = board[1]
                                                    tmp793 = tmp792[1]
                                                    tmp794 = tmp793[1]
                                                    tmp795 = tmp794[1]
                                                    tmp796 = tmp795[1]
                                                    tmp797 = tmp796[1]
                                                    tmp798 = tmp797[1]
                                                    # Result is in tmp798
                                                    return tmp798
                                                else:
                                                    # Generated Python code from LAMBDA compilation
                                                    tmp799 = -1
                                                    # Result is in tmp799
                                                    return tmp799
                                                tmp800 = tmp798
                                                # Result is in tmp800
                                                return tmp800
                                            tmp801 = tmp789
                                            # Result is in tmp801
                                            return tmp801
                                        tmp802 = tmp780
                                        # Result is in tmp802
                                        return tmp802
                                    tmp803 = tmp772
                                    # Result is in tmp803
                                    return tmp803
                                tmp804 = tmp765
                                # Result is in tmp804
                                return tmp804
                            tmp805 = tmp759
                            # Result is in tmp805
                            return tmp805
                        tmp806 = tmp754
                        # Result is in tmp806
                        return tmp806
                    tmp807 = tmp750
                    # Result is in tmp807
                    return tmp807
                # Result is in fun135
                return fun135
            tmp808 = fun134(tmp486)
            tmp809 = 1
            tmp810 = tmp488 - tmp809
            tmp811 = tmp808(tmp810)
            tmp812 = 1
            tmp813 = tmp811 + tmp812
            tmp814 = (tmp813, tmp494)
            tmp815 = (tmp747, tmp814)
            tmp816 = (tmp486, tmp815)
            tmp817 = fun123(tmp816)
            # Result is in tmp817
            return tmp817
        else:
            # Generated Python code from LAMBDA compilation
            # Result is in tmp494
            return tmp494
        tmp818 = tmp817
        # Result is in tmp818
        return tmp818
    tmp819 = tmp743
    # Result is in tmp819
    return tmp819
# Result is in fun123


tmp195 = 0
tmp196 = 0
tmp197 = 0
tmp198 = 0
tmp199 = 0
tmp200 = 0
tmp201 = 0
tmp202 = 0
tmp203 = (tmp201, tmp202)
tmp204 = (tmp200, tmp203)
tmp205 = (tmp199, tmp204)
tmp206 = (tmp198, tmp205)
tmp207 = (tmp197, tmp206)
tmp208 = (tmp196, tmp207)
tmp209 = (tmp195, tmp208)

board = tmp209  # This is the initial empty board

initial_i = 0      # Start at row 0
initial_j = 0      # Start at column 0
initial_nsol = 0   # Start with 0 solutions

search_args = (board, (initial_i, (initial_j, initial_nsol)))

result = fun123(search_args)
print(result)
