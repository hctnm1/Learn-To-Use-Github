pragma solidity >= 0.7.0 < 0.9.0;

contract Employee {
    uint256 salary;
    
    function set(uint256 sal) virtual public {
        salary = sal;
    } 
    
    function get() public virtual view returns(uint256) {
        return salary;
    }
}

contract Clerk is Employee {
    uint256 HRA;
    uint256 DA;
    uint256 TotalSalary;
    
    function set(uint256 s) override(Employee) virtual public{
        super.set(s);
        HRA = (10 * super.get())/100;
        DA = (50 * super.get())/100;
    }
    
    function cal() public {
        TotalSalary = super.get() + HRA + DA;
    }
    
    function get() override(Employee) virtual public view returns(uint256){
        return TotalSalary;
    }
}

contract Officer is Clerk {
    
    function set(uint256 s2) override(Clerk) public{
        super.set(s2);
        HRA = (20 * super.get())/100;
        DA = (50 * super.get())/100;
    }
    
    function cal2() public {
        TotalSalary = super.get() + HRA + DA;
    }
    
    function get() override(Clerk) public view returns(uint256){
        return TotalSalary;
    }
    
    
}