import {mount} from '@vue/test-utils';
import Navbase from "@/components/Navigation.vue"

describe("Tes base navbar", () => {
    const wrapper = mount(Navbase);
    it ("apakah base navbar ada tombol Buat akun", () => {
        const buatAkun_button = wrapper.find({ref: "buatAkun-button"});
        expect(buatAkun_button.exists()).toBe(true);
        expect(wrapper.html()).toContain("Buat akun");
    });

    it ("apakah base navbar ada tombol Login", () => {
        const login_button = wrapper.find({ref:"login"});
        expect(login_button.exists()).toBe(true);
        expect(wrapper.html()).toContain("Login");
    });

    it ("apakah base navbar ada tombol Pengumuman", () => {
        const pengumuman_button = wrapper.find({ref:"pengumuman-button"});
        expect(pengumuman_button.exists()).toBe(true);
        expect(wrapper.html()).toContain("Pengumuman");
    });

    it ("apakah base navbar ada tombol Surat", () => {
        const surat_button = wrapper.find({ref:"surat-button"});
        expect(surat_button.exists()).toBe(true);
        expect(wrapper.html()).toContain("Surat");
    });

    it ("button Surat redirect", () => {
        const button = wrapper.find({ref:"surat-button"});
        window.location.assign = jest.fn();
        button.trigger("click");
        expect(window.location.assign).toHaveBeenCalledWith("/surat");
    });

    it ("button Pengumuman redirect", () => {
        const button = wrapper.find({ref:"pengumuman-button"});
        window.location.assign = jest.fn();
        button.trigger("click");
        expect(window.location.assign).toHaveBeenCalledWith("/pengumuman");
    });


    it ("button Login redirect",() => {
        const button = wrapper.find({ref:"login"});
        window.location.assign = jest.fn();
        button.trigger("click");
        expect(window.location.assign).toHaveBeenCalledWith("/login");
    });
    
    it ("button buat akun redirect", () => {
        const button = wrapper.find({ref:"buat-akun"});
        window.location.assign = jest.fn();
        button.trigger("click");
        expect(window.location.assign).toHaveBeenCalledWith("/buatAkun");
    });

})