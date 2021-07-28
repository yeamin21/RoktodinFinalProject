import "./Home.scss";
export default function Home() {
  return (
    <div className="home">
      <div className="feat">
        Secured
        <div>
          Your personal details (ie: phone no, email) wont be shared unless you
          want to
        </div>
      </div>
      <div className="feat">
        AI Search
        <div>
          Our ML model will help you find the quickest response possible
        </div>
      </div>
      <div className="feat">
        Better UX
        <div>UI is designed with "ease of use" </div>
      </div>
      <div className="feat">
        Multi Platform
        <div>Native application for multiple platform</div>
      </div>
    </div>
  );
}
