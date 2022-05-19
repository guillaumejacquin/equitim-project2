import { Outlet } from "react-router-dom";
import Sidebar from "../sidebar/Sidebar";

const AppLayout = () => {
    return <div style={{
        padding: '0px 0px 0px 20%'
    }}>
        <Sidebar />
        <Outlet />
    </div>;
};

export default AppLayout;
