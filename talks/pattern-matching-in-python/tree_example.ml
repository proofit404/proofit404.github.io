type tree = Leaf of int
          | Node of tree * tree;;

let rec have_in_tree test tree =
  match tree with
  | Leaf x -> test x
  | Node (left, right) ->
     have_in_tree test left
     || have_in_tree test right;;

let mytree = Node(Node(Leaf(0), Leaf(2)), Node(Leaf(3), Leaf(4)));;

let result = have_in_tree (fun x -> x = 0) mytree;;

print_endline (string_of_bool result);;
