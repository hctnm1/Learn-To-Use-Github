<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <h2 class="mt-5">Palindrome Checker</h2><br>

        <div class="row">
            <div class="col-md-5">
                <form method="post">        
                    <div class="mb-3">
                        <label for="exampleFormControlInput1" class="form-label">Input A Number :</label>
                        <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="Input a number" name="num">
                    </div>
                    <button type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Check</button>  <br><br>
                </form> 
            </div>
        </div>
        <?php   
            if($_POST){
                //get from input  
                $num = $_POST['num'];  
                //reverse the number  
                $reverse = strrev($num);  
                
                //checking if the number and reverse is equal  
                if($num == $reverse){  
                    echo "The number $num is Palindrome";     
                }else if($num != $reverse){  
                    echo "The number $num is not a Palindrome";   
                }else{
                    echo "";
                } 
            }     
        ?> 
    </div>



    
</body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</html> 